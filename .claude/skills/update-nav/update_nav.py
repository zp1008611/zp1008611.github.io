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


def locate_insertion(lines: list[str], section_span: tuple[int, int], mkdocs_path: str) -> tuple[int, int, str]:
    section_start, section_end = section_span
    parts = mkdocs_path.split("/")
    prefix2 = "/".join(parts[:2]) + "/" if len(parts) >= 2 else parts[0] + "/"

    # 优先：同二级目录的最后一个条目后插入
    last_similar_idx = None
    last_similar_indent = None
    for i in range(section_start + 1, section_end):
        line = lines[i]
        if line.lstrip().startswith("#") or ".md" not in line:
            continue
        if prefix2 in line:
            last_similar_idx = i
            last_similar_indent = line_indent(line)
    if last_similar_idx is not None and last_similar_indent is not None:
        return last_similar_idx + 1, last_similar_indent, f"按目录 {prefix2.rstrip('/')} 归位"

    # 次优：section 末尾追加
    return section_end, 8, "未命中二级分组，追加到一级 section 末尾"


def yaml_valid(lines: list[str]) -> tuple[bool, str | None]:
    try:
        yaml.compose(dump_lines(lines))
        return True, None
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)


def main() -> int:
    parser = argparse.ArgumentParser(description="Update mkdocs nav entries from changed docs markdown files.")
    parser.add_argument("paths", nargs="*", help="Optional explicit docs paths (relative to repo).")
    args = parser.parse_args()

    if args.paths:
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
        insert_at, indent, reason = locate_insertion(lines, section_span, mkdocs_path)
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
