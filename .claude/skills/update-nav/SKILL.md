---
name: update-nav
description: 根据 docs 变更自动更新 mkdocs.yml 的 nav，按目录推断位置并避免重复。
---

# update-nav 技能

用于在新增/修改 `docs/**/README.md`、`docs/**/index.md` 后，自动把条目补到 `mkdocs.yml` 的 `nav`。

## 工作流程

### 步骤一：识别候选文章

默认扫描当前 git 工作区变更（`git status --porcelain`），筛选：
- `docs/**/README.md`
- `docs/**/index.md`

如用户在命令后附加路径参数，则仅处理指定路径。

### 步骤二：生成导航元数据

对每个候选文件：
1. 将路径转成 mkdocs 形式（去掉 `docs/` 前缀）
2. 读取首个 `# ` 标题作为 label
3. 若无 H1，则回退为目录名（`snake_case`/`kebab-case` 转空格后首字母大写）

### 步骤三：推断 section 并插入 nav

目录映射规则：
- `DL/*` -> `DL`
- `ML/*` -> `ML`
- `RL/*` -> `RL`
- `OROPT/*` -> `运筹与优化`
- `LEETCODE/*` -> `LEETCODE`
- `LLMs_RECORDS/*` -> `大模型技术学习`
- 其余目录 -> 尝试同名一级 section

插入策略：
1. 若 `mkdocs.yml` 已存在相同 path，跳过
2. 优先尝试插入到同二级目录条目后
3. 若未命中二级分组，追加到对应一级 section 末尾
4. 每次插入后进行 YAML 可解析性校验，失败则回退该条并报错

### 步骤四：执行脚本

运行：

```bash
python3 .claude/skills/update-nav/update_nav.py
```

#### 方式一：处理指定文件

```bash
python3 .claude/skills/update-nav/update_nav.py docs/DL/Basics/<new_topic>/README.md
```

#### 方式二：扫描整个文件夹（支持多级目录）

```bash
# 扫描指定文件夹下的所有 README.md/index.md
python3 .claude/skills/update-nav/update_nav.py -a docs/DL/Basics/

# 支持任意层级目录
python3 .claude/skills/update-nav/update_nav.py -a docs/OROPT/or_metaheuristics/
python3 .claude/skills/update-nav/update_nav.py -a docs/LEETCODE/
```

`-a` 参数会递归扫描目标文件夹下的所有 `README.md` 和 `index.md` 文件，并将其添加到 mkdocs.yml 的 nav 中。

### 步骤五：返回结果

输出以下信息：
- 新增了哪些 nav 条目
- 跳过了哪些条目（重复/无法定位/校验失败）

## 注意事项

- 本技能仅做“增量补录”，不重排、不重构现有 `nav`。
- 若遇到历史路径/层级不一致导致无法定位，提示用户手工确认。