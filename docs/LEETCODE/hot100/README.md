# HOT100快速复习思路


## 心得

- dfs显式栈写法
```bash
n = len(adj_matrix)
stack = [start]
visited = set()
while stack:
    node = stack.pop()
    if node not in visited:
        visited.append(node)
        # 这里for循环要在if内，避免节点重复进入stack
        # 比如1和2是邻居，1先入栈，接着就是2入栈，如果for在if外，那么下一次1又会入栈，从而导致死循环
        for i in range(len(adj_matrix[node])):
            if adj_matrix[node][i] and i!=node:
                stack.append(i)
```

- bfs队列写法
```bash
visited = set()
queue = [start]
visited.add(start)
while queue:
    node = queue[0]
    queue = queue[1:]
    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            queue.append(nei)
```

- 01背包问题

```bash
# 问题定义：
有N个物品和一个容量为C的背包。
第i个物品的体积是w[i]，价值是v[i]。
每个物品只能用一次。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。

# 核心特点：
每个物品只能选择0次或1次（0-1选择）

# 状态定义：
dp[i][j] = 前i个物品，背包容量为j时的最大价值

# 状态转移方程：
dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
               不选第i个      选第i个
               
# 边界条件：
dp[0][j] = 0  # 没有物品，价值为0
dp[i][0] = 0  # 背包容量为0，价值为0

# 优化为一维（滚动数组）：
dp[j] = max(dp[j], dp[j-w[i]] + v[i])

# 遍历顺序的关键：
必须倒序遍历容量！
for i in range(N):
    for j in range(C, w[i]-1, -1):  # 倒序！
        dp[j] = max(dp[j], dp[j-w[i]] + v[i])

# 为什么倒序？
倒序保证每个物品只被使用一次
如果正序，dp[j-w[i]]可能已经包含了第i个物品

# 模板代码：
def knapsack_01(N, C, weights, values):
    # 二维DP
    dp = [[0] * (C + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(C + 1):
            dp[i][j] = dp[i-1][j]  # 不选
            if j >= weights[i-1]:
                dp[i][j] = max(dp[i][j], 
                              dp[i-1][j-weights[i-1]] + values[i-1])
    
    return dp[N][C]
    
    # 一维DP优化
    dp = [0] * (C + 1)
    for i in range(N):
        for j in range(C, weights[i]-1, -1):  # 倒序！
            dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
    
    return dp[C]

# 常见变体：
1. 恰好装满：dp[0]=0，其他初始化为-∞
2. 求方案数：dp[j] += dp[j-w[i]]
3. 输出具体方案：记录选择路径
4. 二维费用：dp[i][j][k]（两个约束条件）

# 与完全背包对比：
┌─────────────┬──────────┬──────────┐
│   特性      │  01背包  │ 完全背包 │
├─────────────┼──────────┼──────────┤
│ 物品使用次数│   1次    │  无限次  │
│ 状态转移来源│ dp[i-1]  │  dp[i]   │
│ 一维遍历方向│  倒序    │  正序    │
│ 应用场景    │ 选或不选 │ 凑数问题 │
└─────────────┴──────────┴──────────┘

# LeetCode相关题目：
- 416. 分割等和子集（判断能否凑成target）
- 494. 目标和（添加正负号凑目标）
- 1049. 最后一块石头的重量II
- 474. 一和零（二维费用背包）
```
  

- 完全背包问题

```bash
# 问题定义：
有N种物品和一个容量为C的背包，每种物品都有无限个。
第i种物品的体积是w[i]，价值是v[i]。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。

# 与01背包的区别：
01背包：每个物品只能用一次
完全背包：每个物品可以用无限次

# 状态转移方程：
dp[i][j] = max(dp[i-1][j], dp[i][j-w[i]] + v[i])
               不选第i种      选第i种（可以继续选）
               
# 优化为一维：
dp[j] = max(dp[j], dp[j-w[i]] + v[i])

# 遍历顺序的关键：
01背包：内层倒序（防止重复使用）
完全背包：内层正序（允许重复使用）

# 模板代码：
def complete_knapsack(N, C, weights, values):
    # 二维DP
    dp = [[0] * (C + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(C + 1):
            dp[i][j] = dp[i-1][j]  # 不选
            if j >= weights[i-1]:
                dp[i][j] = max(dp[i][j], dp[i][j-weights[i-1]] + values[i-1])
    return dp[N][C]
    
    # 一维DP优化
    dp = [0] * (C + 1)
    for i in range(N):
        for j in range(weights[i], C + 1):  # 正序！
            dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
    return dp[C]

# 常见变体：
1. 恰好装满：dp[0]=0，其他初始化为-∞或None
2. 求方案数：dp[j] += dp[j-w[i]]
3. 求最少物品数：dp[j] = min(dp[j], dp[j-w[i]]+1)

# LeetCode相关题目：
- 279. 完全平方数（最少个数）
- 322. 零钱兑换（最少硬币数）
- 518. 零钱兑换II（方案数）
- 377. 组合总和IV（排列数）
- 1449. 数位成本和为目标值的最大数字
```

## Reference

- https://leetcode.cn/studyplan/top-100-liked/

- [两数之和](https://leetcode.cn/problems/two-sum/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：找到数组中两个数之和等于目标值target的索引
    - **解法：哈希表（推荐）**
        - 遍历数组，对于每个数`nums[i]`
        - 计算`complement = target - nums[i]`
        - 在哈希表中查找complement
        - 如果找到，返回两个索引
        - 如果没找到，将当前数和索引存入哈希表
    - **关键**：
        - 一次遍历即可（边存边查）
        - 哈希表提供O(1)查找
        - 注意：不能使用同一元素两次
    - 时间O(n) 空间O(n)

- [41. 缺失的第一个正数](https://leetcode.cn/problems/first-missing-positive/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：在未排序数组中找到缺失的第一个正整数，要求O(n)时间和O(1)空间
    - **核心思路：原地哈希**
        - 把数组本身当成哈希表
        - 索引i存储数字i+1（索引0存1，索引1存2...）
    - **算法步骤**：
        1. **整理阶段**：将每个数字放到正确位置
           - 遍历数组，对于nums[i]：
           - 如果1 ≤ nums[i] ≤ n 且不在正确位置
           - 交换到索引nums[i]-1的位置
           - 用while循环直到当前位置无法交换
        2. **检查阶段**：找第一个不匹配的位置
           - 遍历数组，找第一个nums[i] ≠ i+1的位置
           - 返回i+1
        3. **边界情况**：如果都匹配，返回n+1
    - **关键**：
        - 答案必在[1, n+1]范围（鸽笼原理）
            - 最坏情况：数组完美包含 [1, n]，答案是 n+1
            - 其他情况：数组中有"垃圾"数字，答案在 [1, n] 中
        - 交换条件：nums[nums[i]-1] ≠ nums[i]（避免死循环）
        - 忽略≤0、>n、重复的数字
    - 时间O(n) 空间O(1)

- [19.删除链表的倒数第N个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：删除链表的倒数第n个节点，返回链表头节点
    - **解法1：双指针（快慢指针）- 推荐**
        - 使用虚拟头节点dummy，简化删除头节点的情况
        - 快指针fast先走n+1步
        - 然后fast和slow同时走，直到fast到达末尾
        - 此时slow正好在待删除节点的前一个
        - 执行删除：`slow.next = slow.next.next`
        - 时间O(L) 空间O(1)，L为链表长度
    - **解法2：递归（巧妙）**
        - 递归到链表末尾，在回溯时从后往前计数
        - 利用递归栈实现"倒数"
        - 当计数到n时，返回node.next（跳过该节点）
        - 其他节点返回自己并更新next指向
        - 时间O(L) 空间O(L)（递归栈）
    - **关键**：
        - 双指针：快指针先走n+1步（让slow停在待删除节点的前一个）
        - 递归：回溯时计数实现倒数，巧妙利用递归特性
        - 虚拟头节点统一处理边界情况

  
- [21.合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：将两个升序链表合并为一个新的升序链表
    - **解法1：迭代（推荐）**
        - 使用虚拟头节点dummy简化操作
        - 用指针curr维护当前位置
        - 比较两个链表的节点值，选择较小的接到curr后
        - 最后接上剩余部分
        - 时间O(m+n) 空间O(1)
    - **解法2：递归**
        - 递归定义：merge(l1, l2) = 较小的节点 + merge(剩余部分)
        - 终止条件：某个链表为空
        - 时间O(m+n) 空间O(m+n)（递归栈）
    - **关键**：虚拟头节点避免边界判断，迭代比递归更省空间

- [23.合并K个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：合并k个升序链表，返回合并后的升序链表
    - **解法1：最小堆/优先队列（推荐）**
        - 将k个链表的头节点放入最小堆
        - 每次取出堆顶（最小值），接到结果链表
        - 将取出节点的next加入堆
        - 时间O(N log k) 空间O(k)，N为总节点数
    - **解法2：分治合并（最优）**
        - 类似归并排序，两两合并
        - 第一轮：k个链表合并成k/2个
        - 第二轮：k/2个合并成k/4个
        - 直到剩下1个
        - 时间O(N log k) 空间O(log k)（递归栈）
    - **解法3：顺序合并**
        - 依次将链表合并到结果中
        - 时间O(k²N) 空间O(1)
    - **关键**：最小堆实现简单，分治法空间更优


- [24.两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：两两交换链表中相邻的节点，返回交换后的链表头
    - **解法1：迭代（推荐）**
        - 使用虚拟头节点dummy简化操作
        - 维护三个指针：prev（前驱）、first（第一个）、second（第二个）
        - 交换步骤：`prev.next = second`, `first.next = second.next`, `second.next = first`
        - 移动prev到first，继续处理下一对
        - 时间O(n) 空间O(1)
    - **解法2：递归**
        - 递归定义：swap(head) = 交换前两个节点 + swap(剩余部分)
        - 终止条件：链表为空或只有一个节点
        - 时间O(n) 空间O(n)（递归栈）
    - **关键**：
        - 虚拟头节点简化边界处理
        - 迭代法需要仔细处理指针关系（三步交换）
        - 注意处理奇数个节点的情况


- [25.K个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：将链表每k个节点一组进行翻转，不足k个的保持原样
    - **解法：迭代（分步处理）**
        - 使用虚拟头节点dummy简化操作
        - **步骤1**：检查是否有k个节点（用计数或指针移动）
        - **步骤2**：如果有k个节点，翻转这k个节点
        - **步骤3**：连接翻转后的部分与前后链表
        - **步骤4**：移动指针到下一组，重复
        - 时间O(n) 空间O(1)
    - **关键**：
        - 先检查再翻转（不足k个不翻转）
        - 翻转k个节点的标准操作
        - 记录每组的头尾节点，用于连接
        - prev指向当前组的前驱，翻转后移到当前组的尾部

  
- [146.LRU缓存](https://leetcode.cn/problems/lru-cache/?envType=study-plan-v2&envId=top-100-liked)
    - **问题**：实现LRU缓存，支持O(1)时间get和put操作
    - **核心数据结构**：哈希表 + 双向链表
    - **设计思路**：
        - 哈希表：存储key到链表节点的映射，实现O(1)查找
        - 双向链表：维护使用顺序，头部=最近使用，尾部=最久未使用
    - **操作**：
        1. **get(key)**：存在则移到链表头部，返回值；不存在返回-1
        2. **put(key, value)**：存在则更新并移到头部；不存在则插入头部，容量满时删除尾部
    - **关键点**：
        - 双向链表方便O(1)删除任意节点
        - 使用dummy头尾节点简化边界处理
    - **Python技巧**：用`OrderedDict`可简化实现
    - 时间O(1) 空间O(capacity)


- [236.二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked)
    - **问题**：找到二叉树中两个节点p和q的最近公共祖先（LCA）
    - **定义**：LCA是p和q的公共祖先中，离p和q最近的节点（节点可以是自己的祖先）
    - **解法：递归（后序遍历）**
    - **核心思路**：
        1. 从底向上递归，后序遍历（左→右→根）
        2. 如果当前节点是p或q，返回当前节点
        3. 递归左右子树，获取返回值
        4. **判断逻辑**：
            - 左右都不为空 → 当前节点就是LCA
            - 只有左边不为空 → 返回左边结果
            - 只有右边不为空 → 返回右边结果
            - 都为空 → 返回None
    - **关键**：利用后序遍历从底向上传递信息
    - 时间O(n) 空间O(h)  (h为树高)

- [22.括号生成](https://leetcode.cn/problems/generate-parentheses/description/?envType=study-plan-v2&envId=top-100-liked)
    - **问题**：生成n对有效括号的所有组合
    - **解法：回溯（DFS）**
    - **核心思想**：每次选择添加左括号或右括号，通过剪枝保证有效性
    - **剪枝条件**：
        - 左括号数量 `left < n` → 可以添加左括号 `(`
        - 右括号数量 `right < left` → 可以添加右括号 `)`
        - 右括号必须少于左括号（保证有效性）
    - **递归终止**：当 `left == right == n` 时，得到一个有效组合
    - **模板**：`dfs(path, left, right)` → 维护当前路径和左右括号数量
    - 时间O(4^n/√n) 空间O(n)
    

- [79.单词搜索](https://leetcode.cn/problems/word-search/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：在二维网格中搜索单词，可以上下左右移动，不能重复使用同一格子
    - **解法：DFS + 回溯**
    - **核心思路**：
        1. 遍历网格，找到第一个字符匹配的位置作为起点
        2. 从起点开始DFS，尝试匹配剩余字符
        3. 四个方向递归搜索：上、下、左、右
        4. 用**标记**防止重复访问（visited数组 或 原地修改）
        5. 回溯时恢复状态
    - **剪枝条件**：
        - 越界、字符不匹配、已访问 → 返回False
        - 匹配完整单词 → 返回True
    - **优化**：原地修改board标记访问（省空间）
    - 时间O(m·n·3^L) 空间O(L)  (L为单词长度)


- [131.分割回文串](https://leetcode.cn/problems/palindrome-partitioning/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：将字符串分割成若干回文子串，返回所有可能的分割方案
    - **解法：回溯 + 动态规划预处理（可选）**
    - **核心思路**：
        1. 枚举所有可能的分割位置（决策树）
        2. 对每个前缀判断是否为回文
        3. 如果是回文，加入路径，继续递归剩余部分
        4. 到达字符串末尾时，记录当前方案
    - **关键**：
        - `dfs(start)` → 从start位置开始分割
        - 枚举分割点 `i in range(start, n)`
        - 判断 `s[start:i+1]` 是否回文
    - **优化**：DP预处理回文判断，避免重复计算
    - 时间O(n·2^n) 空间O(n²)
    

- [51.N皇后](https://leetcode.cn/problems/n-queens/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：在n×n棋盘上放置n个皇后，使得任意两个皇后不能相互攻击
    - **约束**：皇后可以攻击同行、同列、同对角线上的棋子
    - **解法：回溯**
    - **核心思路**：
        1. 逐行放置皇后（每行只放一个）
        2. 对于第i行，尝试在第j列放置皇后
        3. 检查(i,j)位置是否合法（不与已放置的皇后冲突）
        4. 合法则继续下一行，不合法则回溯
    - **冲突检查**：
        - 列冲突：`cols[j]` 记录第j列是否有皇后
        - 主对角线：`diag1[i-j]` 记录该对角线是否有皇后
        - 副对角线：`diag2[i+j]` 记录该对角线是否有皇后
    - **优化**：用集合/数组标记已占用的列和对角线，O(1)判断冲突
    - 时间O(n!) 空间O(n)
    

- [994.腐烂的橘子](https://leetcode.cn/problems/rotting-oranges/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：腐烂橘子每分钟向四周扩散，求所有橘子腐烂的最少时间
    - **解法：多源BFS（层序遍历）**
    - **核心思路**：
        1. 将所有初始腐烂的橘子加入队列（多个起点）
        2. BFS层序遍历，每层代表一分钟
        3. 腐烂橘子向四周扩散，新鲜橘子变腐烂
        4. 记录扩散的轮数（分钟数）
    - **关键点**：
        - 统计新鲜橘子数量，最后检查是否全部腐烂
        - 用`len(queue)`控制每一层的遍历
        - 四个方向：上下左右
    - **边界情况**：没有新鲜橘子返回0，有新鲜但无法腐烂返回-1
    - 时间O(m·n) 空间O(m·n)
    

- [207.课程表](https://leetcode.cn/problems/course-schedule/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：判断是否可以完成所有课程（有先修课程依赖关系）
    - **本质**：判断有向图是否有环（拓扑排序）
    - **解法1：BFS拓扑排序（Kahn算法）- 推荐**
        1. 统计每个节点的入度
        2. 将入度为0的节点入队（没有前置依赖）
        3. BFS遍历，每次取出节点，将其邻居入度-1
        4. 入度变为0的节点入队
        5. 最后检查是否所有节点都被访问
    - **解法2：DFS检测环**
        - 三色标记法：未访问(0)、访问中(1)、已完成(2)
        - 如果访问到"访问中"的节点，说明有环
    - **关键**：有环→无法完成，无环→可以完成
    - 时间O(V+E) 空间O(V+E)  (V节点数，E边数)

- [208.实现前缀树](https://leetcode.cn/problems/implement-trie-prefix-tree/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：实现Trie树，支持插入、搜索、前缀搜索
    - **核心结构**：树形结构，每个节点代表一个字符
    - **节点设计**：
        - `children`: 字典/数组，存储子节点（26个字母）
        - `is_end`: 布尔值，标记是否为单词结尾
    - **操作**：
        1. **insert(word)**：从根开始，逐字符创建/移动节点，最后标记is_end
        2. **search(word)**：逐字符匹配，检查最后节点的is_end
        3. **startsWith(prefix)**：逐字符匹配，不需要检查is_end
    - **技巧**：用字典`{}`比数组`[None]*26`更灵活
    - 时间O(L) 空间O(N·L)  (L为字符串长度，N为单词数)


- [121.买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：只能买卖一次，求最大利润
    - **解法1：一次遍历（贪心）**
        - 维护历史最低价格`min_price`
        - 遍历时计算`当前价格 - 最低价格`的最大值
    - **解法2：动态规划**
        - `dp[i][0]` = 第i天不持有股票的最大利润
        - `dp[i][1]` = 第i天持有股票的最大利润
    - 时间O(n) 空间O(1)
    
    - **股票问题系列总结**：
        1. **121. 买卖一次**：维护最低价，计算最大利润
        2. **122. 买卖多次**：贪心，所有上涨都买卖
        3. **309. 含冷冻期**：DP三状态（持有、不持有且冷冻、不持有不冷冻）
        4. **714. 含手续费**：DP，卖出时减手续费
        5. **123. 最多2次**：DP，4个状态（第1次买、第1次卖、第2次买、第2次卖）
        6. **188. 最多k次**：DP，2k个状态推广


- [55.跳跃游戏](https://leetcode.cn/problems/jump-game/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：判断能否从第一个位置跳到最后一个位置
    - **你的思路（DP）**：
        - `dp[i]`表示能否到达位置i
        - 从前往后遍历，检查之前的位置k能否跳到i
        - 如果`dp[k]=True`且`nums[k]>=i-k`，则`dp[i]=True`
        - 时间O(n²) 空间O(n)
    - **优化：贪心（更优）**：
        - 维护能到达的最远位置`max_reach`
        - 遍历过程中更新`max_reach = max(max_reach, i+nums[i])`
        - 如果`max_reach >= n-1`返回True
        - 时间O(n) 空间O(1)

- [45.跳跃游戏II](https://leetcode.cn/problems/jump-game-ii/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：求到达最后位置的最少跳跃次数
    - **你的思路（DP）**：
        - `dp[i]`表示到达位置i的最少跳跃次数
        - 初始化`dp[0]=0`，其他为无穷大
        - 对每个位置i，检查所有能跳到i的位置k
        - `dp[i] = min(dp[i], dp[k]+1)`
        - 时间O(n²) 空间O(n)
    - **优化：贪心（更优）**：
        - 每次跳跃选择能到达最远位置的点
        - 维护当前跳跃范围的边界`end`
        - 在边界内更新下一跳能到达的最远距离
        - 时间O(n) 空间O(1)

- [763.划分字母区间](https://leetcode.cn/problems/partition-labels/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：分割字符串为尽可能多的片段，同一字母只出现在一个片段中
    - **解法：贪心（类似跳跃游戏II）**
    - **核心思路**：
        1. 预处理：记录每个字符最后出现的位置`last[char]`
        2. 遍历字符串，维护当前片段必须到达的最远位置`end`
        3. 更新`end = max(end, last[s[i]])`
        4. 当`i == end`时，说明可以切分，记录片段长度
    - **关键**：贪心策略 - 每次尽早切分，保证片段最多
    - **类比**：与45题类似，维护边界，到边界时"跳跃"（切分）
    - 时间O(n) 空间O(1) (字母表大小固定26)


- [70.爬楼梯](https://leetcode.cn/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：n阶楼梯，每次爬1或2个台阶，求有多少种爬法
    - **本质**：斐波那契数列
    - **解法1：动态规划**
        - `dp[i]` = 到达第i阶的方法数
        - `dp[i] = dp[i-1] + dp[i-2]` (从i-1爬1步 或 从i-2爬2步)
        - 初始：`dp[0]=1, dp[1]=1`
        - 时间O(n) 空间O(n)
    - **解法2：空间优化（滚动变量）**
        - 只需记录前两个状态，用两个变量代替数组
        - 时间O(n) 空间O(1)
    - **关键**：第i阶只能从i-1或i-2到达，所以方法数是两者之和


- [118.杨辉三角](https://leetcode.cn/problems/pascals-triangle/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：生成杨辉三角的前n行
    - **核心规律**：
        - 每行首尾都是1
        - 中间元素 = 上一行相邻两数之和
        - `triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]`
    - **解法：逐行构建**
        1. 初始化每行为1
        2. 填充中间元素（利用上一行）
        3. 将当前行加入结果
    - **技巧**：
        - 第i行有i+1个元素（第0行有1个）
        - 可以用一维数组滚动优化
    - 时间O(n²) 空间O(1) (不算输出)
  
  
- [198.打家劫舍](https://leetcode.cn/problems/house-robber/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：不能偷相邻的房屋，求能偷到的最大金额
    - **解法：动态规划**
    - **状态定义**：
        - `dp[i]` = 偷到第i间房时的最大金额
    - **状态转移**：
        - `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
        - 不偷第i间：`dp[i-1]`
        - 偷第i间：`dp[i-2] + nums[i]` (不能偷i-1)
    - **初始化**：`dp[0]=nums[0], dp[1]=max(nums[0], nums[1])`
    - **空间优化**：只需两个变量（prev2, prev1）
    - 时间O(n) 空间O(1)

- [279.完全平方数](https://leetcode.cn/problems/perfect-squares/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：给定正整数n，找到和为n的完全平方数的最少数量
    - **本质**：完全背包问题（物品=完全平方数，可无限使用）
    - **解法1：二维DP（完全背包标准写法）**
        - `dp[i][j]` = 使用前i个完全平方数，凑成和为j的最少数量
        - **状态转移**：
            - 不用第i个：`dp[i][j] = dp[i-1][j]`
            - 用第i个：`dp[i][j] = dp[i][j-i²] + 1`（注意：是dp[i]不是dp[i-1]）
            - 取最小：`dp[i][j] = min(dp[i-1][j], dp[i][j-i²] + 1)`
        - **关键区别**：完全背包从同一行dp[i]转移（可重复使用）
        - 时间O(n·√n) 空间O(n·√n)
    - **解法2：一维DP优化**
        - `dp[j]` = 凑成和为j的最少数量
        - 正序遍历（完全背包特征）：`for j in range(square, n+1)`
        - `dp[j] = min(dp[j], dp[j-square] + 1)`
        - 时间O(n·√n) 空间O(n)
    - **解法3：BFS（最短路径视角）**
        - 把问题看作图：从0到n，每次可以走j²步
        - BFS找最短路径（层数=完全平方数个数）
        - 时间O(n·√n) 空间O(n)
    

- [139.单词拆分](https://leetcode.cn/problems/word-break/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：判断字符串能否被拆分成字典中的单词（单词可以重复使用）
    - **解法1：动态规划**
        - `dp[i]` = 字符串前i个字符能否被拆分
        - `dp[i] = any(dp[j] and s[j:i] in wordDict)` for j < i
        - 初始：`dp[0] = True`（空字符串）
    - **优化**：
        - 用set存储wordDict，O(1)查找
        - 记录已访问位置，避免重复
        - 可以剪枝：只检查字典中存在的长度
    - 时间O(n²) 空间O(n)
  

- [300.最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：找出数组中最长严格递增子序列的长度（子序列不要求连续）
    - **解法1：动态规划**
        - `dp[i]` = 以nums[i]结尾的最长递增子序列长度
        - `dp[i] = max(dp[j] + 1)` for all j < i where nums[j] < nums[i]
        - 初始：`dp[i] = 1`（每个元素本身长度为1）
        - 答案：`max(dp)`
        - 时间O(n²) 空间O(n)
    - **解法2：贪心+二分（最优）**
        - 维护一个递增数组tails，tails[i]表示长度为i+1的递增子序列的最小末尾元素
        - 遍历nums[i]，如果大于tails最后元素，append；否则二分查找替换
        - 时间O(n log n) 空间O(n)
    - **关键**：
        - 子序列不连续，可以跳过元素
        - dp[i]依赖所有j<i的结果


- [152.乘积最大子数组](https://leetcode.cn/problems/maximum-product-subarray/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：找出数组中乘积最大的连续子数组，返回最大乘积
    - **核心难点**：负数乘以负数会变成正数
    - **解法：动态规划（维护最大和最小）**
        - 同时维护两个状态：
            - `max_prod` = 以当前位置结尾的最大乘积
            - `min_prod` = 以当前位置结尾的最小乘积
        - **状态转移**：
            - `max_prod = max(nums[i], max_prod * nums[i], min_prod * nums[i])`
            - `min_prod = min(nums[i], max_prod * nums[i], min_prod * nums[i])`
        - **关键**：负数可能让最小变最大，所以要同时维护
    - **优化**：只需两个变量（滚动）
    - 时间O(n) 空间O(1)

- [32.最长有效括号](https://leetcode.cn/problems/longest-valid-parentheses/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：找出最长有效（格式正确且连续）括号子串的长度
    - **解法1：动态规划（推荐）**
        - `dp[i]` = 以s[i]结尾的最长有效括号长度
        - 只有`s[i]=')'`时才可能形成有效括号
        - **状态转移**：
            - 如果`s[i-1]='('`：`dp[i] = dp[i-2] + 2`（配对）
            - 如果`s[i-1]=')'`且`s[i-dp[i-1]-1]='('`：`dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2`（跨越）
        - 时间O(n) 空间O(n)
    - **解法2：栈（巧妙）**
        - 栈底保持最后一个未匹配的`)`的索引
        - 遍历字符串，`(`入栈，`)`出栈并计算长度
        - 时间O(n) 空间O(n)
    - **解法3：双向扫描（最优空间）**
        - 从左到右扫描，统计左右括号数量
        - 从右到左再扫描一次
        - 时间O(n) 空间O(1)

- [5.最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：找出字符串中最长的回文子串
    - **解法1：中心扩散（推荐）**
        - 枚举每个位置作为回文中心，向两边扩散
        - 注意回文中心有两种：单个字符（奇数长度）、两个字符（偶数长度）
        - 对每个中心，只要两边字符相等就继续扩散
        - 时间O(n²) 空间O(1)
    - **解法2：动态规划**
        - `dp[i][j]` = s[i:j+1]是否为回文
        - `dp[i][j] = (s[i]==s[j]) and dp[i+1][j-1]`
        - 按长度从小到大遍历
        - 时间O(n²) 空间O(n²)
    - **解法3：Manacher算法**
        - 最优解法，时间O(n)，但实现复杂
    - **关键**：中心扩散最易理解和实现


- [1143.最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：找出两个字符串的最长公共子序列长度（子序列不要求连续）
    - **解法：动态规划（经典二维DP）**
        - `dp[i][j]` = text1[0:i]和text2[0:j]的最长公共子序列长度
        - **状态转移**：
            - 如果`text1[i-1] == text2[j-1]`：`dp[i][j] = dp[i-1][j-1] + 1`（匹配，加1）
            - 否则：`dp[i][j] = max(dp[i-1][j], dp[i][j-1])`（不匹配，取最大）
        - **初始化**：`dp[0][j] = dp[i][0] = 0`（空串的LCS为0）
        - 时间O(m·n) 空间O(m·n)
    - **优化**：可以用滚动数组优化空间到O(min(m,n))
    - **关键**：
        - 子序列≠子串（不要求连续）
        - 匹配时从dp[i-1][j-1]转移
        - 不匹配时从上方或左方取最大

- [72.编辑距离](https://leetcode.cn/problems/edit-distance/description/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：将word1转换成word2所需的最少操作数（插入、删除、替换）
    - **解法：动态规划（经典二维DP）**
        - `dp[i][j]` = word1的前i个字符转换成word2的前j个字符所需的最少操作数
        - **状态转移**：
            - 如果`word1[i-1] == word2[j-1]`：`dp[i][j] = dp[i-1][j-1]`（不需要操作）
            - 否则三种操作取最小：
                - 插入：`dp[i][j-1] + 1`
                - 删除：`dp[i-1][j] + 1`
                - 替换：`dp[i-1][j-1] + 1`
        - **初始化**：
            - `dp[i][0] = i`（word2为空，需要删除i次）
            - `dp[0][j] = j`（word1为空，需要插入j次）
        - 时间O(m·n) 空间O(m·n)
    - **关键**：理解三种操作对应的DP转移方向

- [31.下一个排列](https://leetcode.cn/problems/next-permutation/?envType=study-plan-v2&envId=top-100-liked)

    - **问题**：找到数组的下一个字典序更大的排列，原地修改
    - **核心思路（三步走）**：
        1. **从后向前找**第一个升序对(i, i+1)，即`nums[i] < nums[i+1]`
        2. **从后向前找**第一个大于`nums[i]`的数`nums[j]`
        3. **交换**`nums[i]`和`nums[j]`，然后**反转**i+1到末尾的部分
    - **关键理解**：
        - 从后往前找，保证增量最小（字典序刚好大一点）
        - i右侧是降序的，交换后仍是降序，需反转变升序（最小排列）
        - 如果找不到升序对，说明是最大排列，反转整个数组
    - **边界情况**：已是最大排列(如[3,2,1])，反转变最小排列
    - 时间O(n) 空间O(1)

