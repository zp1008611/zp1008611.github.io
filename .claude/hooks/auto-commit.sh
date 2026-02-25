#!/bin/bash
# Stop hook: 任务完成后自动检测未提交变更并触发 commit skill

# 默认 Git 身份（可通过环境变量覆盖）
export GIT_AUTHOR_NAME="${GIT_AUTHOR_NAME:-zp1008611}"
export GIT_AUTHOR_EMAIL="${GIT_AUTHOR_EMAIL:-1658763666@qq.com}"
export GIT_COMMITTER_NAME="${GIT_COMMITTER_NAME:-$GIT_AUTHOR_NAME}"
export GIT_COMMITTER_EMAIL="${GIT_COMMITTER_EMAIL:-$GIT_AUTHOR_EMAIL}"

INPUT=$(cat)
STOP_HOOK_ACTIVE=$(echo "$INPUT" | jq -r '.stop_hook_active // false')

# 防止无限循环：commit 后再次触发时直接放行
if [ "$STOP_HOOK_ACTIVE" = "true" ]; then
  exit 0
fi

# 检查是否超过 3 次阻止尝试（防止无限循环）
COMMIT_HOOK_COUNTER_FILE="$CLAUDE_PROJECT_DIR/.claude/hooks/.commit-hook-counter"
if [ -f "$COMMIT_HOOK_COUNTER_FILE" ]; then
  BLOCK_COUNT=$(cat "$COMMIT_HOOK_COUNTER_FILE")
else
  BLOCK_COUNT=0
fi

# 如果已经是第 3 次阻止，放行并重置计数器
if [ "$BLOCK_COUNT" -ge 3 ]; then
  rm -f "$COMMIT_HOOK_COUNTER_FILE"
  exit 0
fi

# 检查是否有未提交的变更
cd "$CLAUDE_PROJECT_DIR" 2>/dev/null || exit 0

# 检查工作区是否有变更（已修改、新文件等）
if git diff --quiet 2>/dev/null && git diff --cached --quiet 2>/dev/null && [ -z "$(git ls-files --others --exclude-standard 2>/dev/null)" ]; then
  # 没有变更，正常结束
  exit 0
fi

# 有未提交变更，阻止 Claude 停止，让它继续执行 commit
# 增加阻止计数
BLOCK_COUNT=$((BLOCK_COUNT + 1))
echo "$BLOCK_COUNT" > "$COMMIT_HOOK_COUNTER_FILE"

cat <<EOF
{"decision": "block", "reason": "检测到未提交的变更，请调用 /commit 技能提交更新。（第 $BLOCK_COUNT/3 次）"}
EOF
