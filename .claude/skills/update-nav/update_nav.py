#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

import yaml

ROOT = Path(__file__).resolve().parents[3]
MKDOCS_FILE = ROOT / "mkdocs.yml"

SECTION_MAP = {
    "DL": "DL",
    "ML": "ML",
    "RL": "RL",
    "OROPT": "运筹与优化",
    "LEETCODE": "LEETCODE",
    "LLMs_RECORDS": "大模型技术学习",
}


def git_changed_docs_files() -> list[Path]:
    cmd = ["git", "-C", str(ROOT), "status", "--porcelain"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    files: list[Path] = []
    for raw in result.stdout.splitlines():
        if not raw:
            continue
        entry = raw[3:]
        if " -> " in entry:
            entry = entry.split(" -> ", 1)[1]
        path = Path(entry)

        if is_candidate(path):
            files.append(path)
            continue

        # git status 对全新目录可能只显示目录本身，这里递归补齐候选 markdown
        abs_path = ROOT / path
        if path.parts and path.parts[0] == "docs" and abs_path.is_dir():
            for matched in abs_path.rglob("*.md"):
                rel = matched.relative_to(ROOT)
                if is_candidate(rel):
                    files.append(rel)

    return sorted(set(files))


def is_candidate(path: Path) -> bool:
    if len(path.parts) < 2:
        return False
    if path.parts[0] != "docs":
        return False
    return path.name in {"README.md", "index.md"}


def normalize_input_paths(paths: Iterable[str]) -> list[Path]:
    result: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_absolute():
            p = p.resolve().relative_to(ROOT)
        if not is_candidate(p):
            continue
        result.append(p)
    return sorted(set(result))


def extract_h1(md_path: Path) -> str | None:
    abs_path = ROOT / md_path
    if not abs_path.exists():
        return None
    try:
        text = abs_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = abs_path.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines():
        match = re.match(r"^\s*#\s+(.+?)\s*$", line)
        if match:
            return re.sub(r"\s+#*\s*$", "", match.group(1)).strip()
    return None


def fallback_label(md_path: Path) -> str:
    folder = md_path.parent.name if md_path.stem.lower() == "index" else md_path.parent.name
    clean = folder.replace("_", " ").replace("-", " ").strip()
    if not clean:
        clean = md_path.stem
    return " ".join(word.capitalize() for word in clean.split())


def to_mkdocs_path(md_path: Path) -> str:
    return str(md_path.relative_to("docs")).replace("\\", "/")


def infer_section_name(mkdocs_path: str) -> str:
    top = mkdocs_path.split("/", 1)[0]
    return SECTION_MAP.get(top, top)


def load_lines() -> list[str]:
    return MKDOCS_FILE.read_text(encoding="utf-8").splitlines(keepends=True)


def dump_lines(lines: list[str]) -> str:
    return "".join(lines)


def find_nav_span(lines: list[str]) -> tuple[int, int]:
    nav_start = None
    for i, line in enumerate(lines):
        if re.match(r"^nav:\s*$", line):
            nav_start = i
            break
    if nav_start is None:
        raise ValueError("mkdocs.yml 中未找到 nav: 节点")

    nav_end = len(lines)
    top_key = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*\s*:\s*(#.*)?$")
    for i in range(nav_start + 1, len(lines)):
        line = lines[i]
        if line.startswith(" ") or line.startswith("\t"):
            continue
        if line.lstrip().startswith("#") or not line.strip():
            continue
        if top_key.match(line.rstrip("\n")):
            nav_end = i
            break
    return nav_start, nav_end


def find_section_span(lines: list[str], nav_span: tuple[int, int], section: str) -> tuple[int, int] | None:
    nav_start, nav_end = nav_span
    section_re = re.compile(r"^\s{4}-\s+(.+):\s*(#.*)?$")
    section_start = None
    for i in range(nav_start + 1, nav_end):
        m = section_re.match(lines[i].rstrip("\n"))
        if m and m.group(1).strip() == section:
            section_start = i
            break
    if section_start is None:
        return None

    section_end = nav_end
    for i in range(section_start + 1, nav_end):
        if section_re.match(lines[i].rstrip("\n")):
            section_end = i
            break
    return section_start, section_end


def has_path(lines: list[str], mkdocs_path: str) -> bool:
    path_re = re.compile(rf"{re.escape(mkdocs_path)}\s*(#.*)?$")
    for line in lines:
        if line.lstrip().startswith("#"):
            continue
        if path_re.search(line.rstrip("\n")):
            return True
    return False


def line_indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def find_subsection(lines: list[str], section_start: int, section_end: int, subsection_name: str) -> tuple[int, int, int] | None:
    """查找指定subsection的位置和范围，返回 (subsection_header行号, 起始缩进, 结束行号)"""
    subsection_re = re.compile(r"^(\s*)- " + re.escape(subsection_name) + r":\s*(#.*)?$")

    for i in range(section_start + 1, section_end):
        line = lines[i]
        if line.lstrip().startswith("#"):
            continue
        m = subsection_re.match(line.rstrip("\n"))
        if m:
            indent = len(m.group(1))
            # 找到subsection header，现在找它的结束位置
            sub_end = section_end
            base_indent = indent + 4  # nested items are 4 more indent
            for j in range(i + 1, section_end):
                sub_line = lines[j]
                if sub_line.lstrip().startswith("#") or not sub_line.strip():
                    continue
                sub_indent = line_indent(sub_line)
                if sub_indent <= indent:
                    sub_end = j
                    break
            return i, indent, sub_end
    return None


def kebab_to_title(name: str) -> str:
    """将 kebab-case 或 snake_case 转换为标题格式"""
    clean = name.replace("_", " ").replace("-", " ").strip()
    return " ".join(word.capitalize() for word in clean.split())


def find_actual_section_end(lines: list[str], section_start: int, nav_end: int) -> int:
    """找到 section 的实际结束位置（最后一个有效内容行）"""
    # section header indent
    header_indent = line_indent(lines[section_start])

    actual_end = section_start + 1
    for i in range(section_start + 1, nav_end):
        line = lines[i]
        # Skip blank lines and comments
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        indent = line_indent(line)
        # If we hit another section header at same or lower indent, stop
        if indent <= header_indent:
            break
        actual_end = i + 1

    return actual_end


def locate_insertion(lines: list[str], section_span: tuple[int, int], mkdocs_path: str, nav_end: int) -> tuple[int, int, str]:
    section_start, _ = section_span

    # 使用实际 section 结束位置
    section_end = find_actual_section_end(lines, section_start, nav_end)

    parts = mkdocs_path.split("/")

    # 需要至少二级目录才有可能创建 subsection
    if len(parts) < 2:
        # 单级目录，直接追加
        default_indent = 12
        for i in range(section_end - 1, section_start, -1):
            line = lines[i]
            if line.lstrip().startswith("#") or not line.strip():
                continue
            if ".md" in line:
                default_indent = line_indent(line)
                break
        return section_end, default_indent, "单级目录，追加到 section 末尾"

    prefix2 = parts[0] + "/" + parts[1] + "/"
    subsection_name = parts[1]

    # 优先：查找同二级目录的已有条目
    for i in range(section_start + 1, section_end):
        line = lines[i]
        if line.lstrip().startswith("#") or ".md" not in line:
            continue
        if prefix2 in line:
            indent = line_indent(line)
            return i + 1, indent, f"按目录 {subsection_name} 归位"

    # 次优：查找是否存在对应的 subsection
    subsection = find_subsection(lines, section_start, section_end, subsection_name)
    if subsection:
        sub_header_idx, sub_indent, sub_end = subsection
        return sub_end, sub_indent + 4, f"插入到现有 subsection {subsection_name}"

    # 三优：section 中现有条目的缩进层级
    default_indent = 12
    for i in range(section_end - 1, section_start, -1):
        line = lines[i]
        if line.lstrip().startswith("#") or not line.strip():
            continue
        if ".md" in line:
            default_indent = line_indent(line)
            break

    # 如果 section 末尾有嵌套内容，需要在嵌套内容之后创建新的 subsection
    # 返回特殊标记，让调用者处理
    return section_end, default_indent, f"需要创建新 subsection: {subsection_name}"


def yaml_valid(lines: list[str]) -> tuple[bool, str | None]:
    try:
        yaml.compose(dump_lines(lines))
        return True, None
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)


def scan_folder(folder: Path) -> list[Path]:
    """扫描指定文件夹下的所有候选 markdown 文件"""
    if folder.parts[0] != "docs":
        folder = Path("docs") / folder

    abs_path = ROOT / folder
    if not abs_path.is_dir():
        return []

    files: list[Path] = []
    for matched in abs_path.rglob("*.md"):
        rel = matched.relative_to(ROOT)
        if is_candidate(rel):
            files.append(rel)

    return sorted(set(files))


def main() -> int:
    parser = argparse.ArgumentParser(description="Update mkdocs nav entries from changed docs markdown files.")
    parser.add_argument("paths", nargs="*", help="Optional explicit docs paths (relative to repo).")
    parser.add_argument("-a", "--all", dest="folder", type=str,
                        help="扫描指定文件夹下的所有 README.md/index.md 文件")
    args = parser.parse_args()

    if args.folder:
        candidates = scan_folder(Path(args.folder))
    elif args.paths:
        candidates = normalize_input_paths(args.paths)
    else:
        candidates = git_changed_docs_files()

    if not candidates:
        print("[update-nav] 未发现候选文件（docs/**/README.md 或 docs/**/index.md）。")
        return 0

    lines = load_lines()
    nav_span = find_nav_span(lines)

    added: list[tuple[str, str, str, str]] = []
    skipped: list[tuple[str, str]] = []

    for md_file in candidates:
        mkdocs_path = to_mkdocs_path(md_file)

        if has_path(lines, mkdocs_path):
            skipped.append((mkdocs_path, "已存在于 nav，跳过"))
            continue

        section_name = infer_section_name(mkdocs_path)
        section_span = find_section_span(lines, nav_span, section_name)
        if section_span is None:
            skipped.append((mkdocs_path, f"未找到 section: {section_name}，请手动确认"))
            continue

        label = extract_h1(md_file) or fallback_label(md_file)
        insert_at, indent, reason = locate_insertion(lines, section_span, mkdocs_path, nav_span[1])

        # 处理需要创建新 subsection 的情况
        if reason.startswith("需要创建新 subsection:"):
            subsection_name = reason.split(":", 1)[1].strip()
            title = kebab_to_title(subsection_name)
            # 新 subsection header 应该在 section header 下面（8-space indent，与 Agentic-RL 同级）
            # 而不是嵌套在现有内容下面（12-space indent）
            # 如果 indent >= 12，说明是嵌套在内容中，需要使用 8-space
            if indent >= 12:
                sub_indent = 8  # section item level
            else:
                sub_indent = indent
            sub_header = f"{' ' * sub_indent}- {title}:\n"
            item_entry = f"{' ' * (sub_indent + 4)}- {label}: {mkdocs_path}\n"
            trial = lines[:insert_at] + [sub_header, item_entry] + lines[insert_at:]
            ok, err = yaml_valid(trial)
            if not ok:
                skipped.append((mkdocs_path, f"创建 subsection 失败：{err}"))
                continue
            lines = trial
            nav_span = find_nav_span(lines)
            added.append((label, mkdocs_path, section_name, f"创建新 subsection: {title}"))
            continue

        entry = f"{' ' * indent}- {label}: {mkdocs_path}\n"

        trial = lines[:insert_at] + [entry] + lines[insert_at:]
        ok, err = yaml_valid(trial)
        if not ok:
            skipped.append((mkdocs_path, f"插入后 YAML 校验失败：{err}"))
            continue

        lines = trial
        nav_span = find_nav_span(lines)
        added.append((label, mkdocs_path, section_name, reason))

    if added:
        MKDOCS_FILE.write_text(dump_lines(lines), encoding="utf-8")

    print("[update-nav] 处理完成")
    if added:
        print("新增条目:")
        for label, path, section, reason in added:
            print(f"- [{section}] {label} -> {path} ({reason})")

    if skipped:
        print("跳过条目:")
        for path, reason in skipped:
            print(f"- {path}: {reason}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
