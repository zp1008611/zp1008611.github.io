# 机考有关的LC题目

## Reference

- https://www.algomooc.com/home

以下的标题的年份对应的是华为机考时间


## 高频题目

- 拼车
- 分割等和子集
- 字符串解码
- 课程表及其变形
- 可能的二分法
- 最小路径和
- 跳跃游戏及其变形
- 规划兼职工作
- 最短超级串
- 最小高度树
- 网络延迟时间
- 01矩阵
- 腐烂的橘子
- 访问所有节点的最短路径
- 分割数组的最大值
- 最大二叉树
- 最后一块石头的重量II
- 无重叠区间


## 高频题型


### 动态规划

- 规划兼职工作
- 最短超级串
- 访问所有节点的最短路径
- 最长重复子数组
- 零钱兑换II
- 盈利计划
- 打家劫舍III
- 最低加油次数
- 最低票价
- 组合总和
- 最小不兼容性
- 分割等和子集
- 最后一块石头的重量II
- 网格中的最短路径
- 俄罗斯套娃信封问题
- 堆叠长方体的最大高度
- 无重叠区间
- 最小路径和
- 摘樱桃

### DFS

- 组合总和III
- 最小高度树
- 腐烂的橘子
- 二叉树的直径
- 路径总和
- 铺瓷砖
- 图像渲染
- 单词搜索II
- 二叉树中所有距离为K的结点
- 监控二叉树
- 矩阵中的最长递增路径
- 口算难题
- 子集
- 二叉树的坡度
- 出现次数最多的子树元素和
- 组合
- 优美的排列
- 括号的分数


### 树

- 将有序数组转换为二叉树
- 监控二叉树
- 最小高度树
- 二叉树的直径
- 二叉搜索树中的搜索
- 二叉树的坡度
- 出现次数最多的子树元素和
- 平衡二叉树
- 树上的操作
- 寻找重复的子树
- 最大二叉树
- 二叉树的层序遍历
- 二叉树中所有距离为K的结点
- 所有可能的真二叉树
- 路径总和

### 栈

- 验证栈的序列
- 每日温度
- 下一个更大的元素I
- 设计循环队列
- 有效的括号
- 文件的最长绝对路径
- 检查替换后的词是否有效
- 删除字符串中的所有相邻重复项II
- 字符串解码
- 找到字符串中第一个匹配项的下标
- 去除重复字母
- 简化路径
- 删除最外层的括号
- 基本计算器
- 小行星碰撞
- 函数的独占时间
- 最小栈


### BFS

- 腐烂的橘子
- 访问所有节点的最短路径
- 被围绕的区域
- 岛屿数量
- 单词接龙
- 最小基因变化
- 所有可能的路径
- 二进制矩阵中的最短路径
- 01矩阵
- 最短的桥
- 公交路线
- 判断二分图
- 可能的二分法
- 寻找峰值II
- 推箱子
- 网格中的最短路径

## Dijkstra

- 网络延迟时间

### 排序

- 根据字符出现频率排序
- 项目管理

### 二分

- 爱吃香蕉的珂珂
- 使结果不超过阈值的最小除数
- 最小体力消耗路径
- 无重叠区间
- 分割数组的最大值
- 水位上升的泳池中游泳


## 滑动窗口

- 字符串的排列
- 快乐数
- 长度最小的子数组
- 最大连续1的个数
- 最大连续1的个数III
- 滑动窗口的最大值
- 可获得的最大点数




## 数论补充

- 模运算：https://leetcode.cn/discuss/post/3584387/fen-xiang-gun-mo-yun-suan-de-shi-jie-dan-7xgu/
- https://leetcode.cn/discuss/post/3584388/fen-xiang-gun-ti-dan-shu-xue-suan-fa-shu-gcai/


## 位运算补充

- https://leetcode.cn/discuss/post/3580371/
- https://leetcode.cn/discuss/post/3571304/cong-ji-he-lun-dao-wei-yun-suan-chang-ji-enve/

## 其他补充

### 矩阵快速幂优化 DP

## 20240821

- DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。例如，"ACGAATTCCG" 是一个 DNA序列 。在研究 DNA 时，识别 DNA 中的重复序列非常有用。给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序 返回答案。[187.重复的DNA序列](https://leetcode.cn/problems/repeated-dna-sequences/description/)

- 给你一个数组 events，其中 events[i] = [startDayi, endDayi] ，表示会议 i 开始于 startDayi ，结束于 endDayi 。你可以在满足 startDayi <= d <= endDayi 中的任意一天 d 参加会议 i 。在任意一天 d 中只能参加一场会议。请你返回你可以参加的 最大 会议数目。[1353.最多可以参加的会议数目](https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended/description/)



## 20240828

- 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。[1094.拼车](https://leetcode.cn/problems/car-pooling/description/)

- 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。请你设计并实现时间复杂度为 O(n) 的算法解决此问题。[128.最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/description/)

- 给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。[946.验证栈序列](https://leetcode.cn/problems/validate-stack-sequences/description/)

- 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。[316.去除重复字母](https://leetcode.cn/problems/remove-duplicate-letters/description/)



## 20240904

- 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。返回矩阵中 省份 的数量。[547.省份数量](https://leetcode.cn/problems/number-of-provinces/description/)

- 给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1 。[1293.网格中的最短路径](https://leetcode.cn/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/)

- 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）[102.二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/description/)

- 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。[347.前k个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/description/)



## 20240911

- 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，两者长度都是 n ，再给你一个正整数 k 。你必须从 nums1 中选一个长度为 k 的 子序列 对应的下标。对于选择的下标 i0 ，i1 ，...， ik - 1 ，你的 分数 定义如下：nums1 中下标对应元素求和，乘以 nums2 中下标对应元素的 最小值 。用公式表示： (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]) 。
请你返回 最大 可能的分数。一个数组的 子序列 下标是集合 {0, 1, ..., n-1} 中删除若干元素得到的剩余集合，也可以不删除任何元素。[2542.最大子序列的分数](https://leetcode.cn/problems/maximum-subsequence-score/description/)

- 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。请实现 KthLargest 类：KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。[703.数据流中的第K大元素](https://leetcode.cn/problems/kth-largest-element-in-a-stream/description/)

- 给定两个整数 n 和 k，以及两个长度为 n 的整数数组 speed 和 efficiency。现有 n 名工程师，编号从 1 到 n。其中 speed[i] 和 efficiency[i] 分别代表第 i 位工程师的速度和效率。从这 n 名工程师中最多选择 k 名不同的工程师，使其组成的团队具有最大的团队表现值。团队表现值 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。请你返回该团队的​​​​​​最大团队表现值，由于答案可能很大，请你返回结果对 10^9 + 7 取余后的结果。[1383.最大的团队表现值](https://leetcode.cn/problems/maximum-performance-of-a-team/description/)

- 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。注意：不允许旋转信封。[354.俄罗斯套娃信封问题](https://leetcode.cn/problems/russian-doll-envelopes/description/)

- 给你 n 个长方体 cuboids ，其中第 i 个长方体的长宽高表示为 cuboids[i] = [widthi, lengthi, heighti]（下标从 0 开始）。请你从 cuboids 选出一个 子集 ，并将它们堆叠起来。如果 widthi <= widthj 且 lengthi <= lengthj 且 heighti <= heightj ，你就可以将长方体 i 堆叠在长方体 j 上。你可以通过旋转把长方体的长宽高重新排列，以将它放在另一个长方体上。返回 堆叠长方体 cuboids 可以得到的 最大高度 。[1691.堆叠长方体的最大高度](https://leetcode.cn/problems/maximum-height-by-stacking-cuboids/description/)


- 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。两个相邻元素间的距离为 1 。[542.01矩阵](https://leetcode.cn/problems/01-matrix/description/)


- 你打算利用空闲时间来做兼职工作赚些零花钱。这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。注意，时间上出现重叠的 2 份工作不能同时进行。如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。[1235.规划兼职工作](https://leetcode.cn/problems/maximum-profit-in-job-scheduling/description/)

- 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。注意 只在一点上接触的区间是 不重叠的。例如 [1, 2] 和 [2, 3] 是不重叠的。[435.无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/description/)

- 给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为 更加简洁的规范路径。在 Unix 风格的文件系统中规则如下：一个点 '.' 表示当前目录本身。此外，两个点 '..' 表示将目录切换到上一级（指向父目录）。任意多个连续的斜杠（即，'//' 或 '///'）都被视为单个斜杠 '/'。任何其他格式的点（例如，'...' 或 '....'）均被视为有效的文件/目录名称。返回的 简化路径 必须遵循下述格式：始终以斜杠 '/' 开头。两个目录名之间必须只有一个斜杠 '/' 。最后一个目录名（如果存在）不能 以 '/' 结尾。此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。返回简化后得到的 规范路径 。[71.简化路径](https://leetcode.cn/problems/simplify-path/description/)


- 有效括号字符串为空 ""、"(" + A + ")" 或 A + B ，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。如果有效字符串 s 非空，且不存在将其拆分为 s = A + B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。给出一个非空有效字符串 s，考虑将其进行原语化分解，使得：s = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。对 s 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 s 。[1021.删除最外层的括号](https://leetcode.cn/problems/remove-outermost-parentheses/description/)

- 珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。[875.爱吃香蕉的珂珂](https://leetcode.cn/problems/koko-eating-bananas/description/)


## 20240913

- 给定一个经过编码的字符串，返回它解码后的字符串。编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。[394.字符串解码](https://leetcode.cn/problems/decode-string/description/)

- 集团里有 n 名员工，他们可以完成各种各样的工作创造利润。第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。[879.盈利计划](https://leetcode.cn/problems/profitable-schemes/description/)

- 有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：如果 x == y，那么两块石头都会被完全粉碎；如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。[1049.最后一块石头的重量II](https://leetcode.cn/problems/last-stone-weight-ii/description/)


## 20240919

- 给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:创建一个根节点，其值为 nums 中的最大值。递归地在最大值 左边 的 子数组前缀上 构建左子树。递归地在最大值 右边 的 子数组后缀上 构建右子树。返回 nums 构建的 最大二叉树 。[654.最大二叉树](https://leetcode.cn/problems/maximum-binary-tree/description/)

- 给你一个大小为 m x n 的整数矩阵 mat 和一个整数 target 。从矩阵的 每一行 中选择一个整数，你的目标是 最小化 所有选中元素之 和 与目标值 target 的 绝对差 。返回 最小的绝对差 。a 和 b 两数字的 绝对差 是 a - b 的绝对值。[1981.最小化目标值与所选元素的差](https://leetcode.cn/problems/minimize-the-difference-between-target-and-chosen-elements/description/)

- 有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：如果 x == y，那么两块石头都会被完全粉碎；如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。[1049.最后一块石头的重量II](https://leetcode.cn/problems/last-stone-weight-ii/description/)

- nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。[496.下一个更大元素I]

- 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。[54.螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/description/)

- 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。[59.螺旋矩阵II](https://leetcode.cn/problems/spiral-matrix-ii/description/)

- 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。[224.基本计算器](https://leetcode.cn/problems/basic-calculator/description/)

- 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。整数除法仅保留整数部分。你可以假设给定的表达式总是有效的。所有中间结果将在 [-231, 231 - 1] 的范围内。注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。[227.基本计算器II](https://leetcode.cn/problems/basic-calculator-ii/description/)

- 在一个 n x n 的整数矩阵 grid 中，每一个方格的值 grid[i][j] 表示位置 (i, j) 的平台高度。当开始下雨时，在时间为 t 时，水池中的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。你从坐标方格的左上平台 (0，0) 出发。返回 你到达坐标方格的右下平台 (n-1, n-1) 所需的最少时间 。[778.水位上升的泳池中游泳](https://leetcode.cn/problems/swim-in-rising-water/description/)

- 你准备参加一场远足活动。给你一个二维 rows x columns 的地图 heights ，其中 heights[row][col] 表示格子 (row, col) 的高度。一开始你在最左上角的格子 (0, 0) ，且你希望去最右下角的格子 (rows-1, columns-1) （注意下标从 0 开始编号）。你每次可以往 上，下，左，右 四个方向之一移动，你想要找到耗费 体力 最小的一条路径。一条路径耗费的 体力值 是路径上相邻格子之间 高度差绝对值 的 最大值 决定的。请你返回从左上角走到右下角的最小 体力消耗值 。[1631.最小体力消耗路径](https://leetcode.cn/problems/path-with-minimum-effort/description/)

## 20240925

- 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... 这样的车站路线行驶。现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。[815.公交路线](https://leetcode.cn/problems/bus-routes/description/)

- 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。你可以按 任何顺序 返回答案。[77.组合](https://leetcode.cn/problems/combinations/description/)

- 假设有从 1 到 n 的 n 个整数。用这些整数构造一个数组 perm（下标从 1 开始），只要满足下述条件 之一 ，该数组就是一个 优美的排列 ：perm[i] 能够被 i 整除 i 能够被 perm[i] 整除给你一个整数 n ，返回可以构造的 优美排列 的 数量 。[526.优美的排列](https://leetcode.cn/problems/beautiful-arrangement/description/)

- 给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是 按字符 ASCII 顺序排列 的邮箱地址。账户本身可以以 任意顺序 返回。[721.账户合并](https://leetcode.cn/problems/accounts-merge/description/)

- 给你两个整数 m 和 n 。构造一个 m x n 的网格，其中每个单元格最开始是白色。请你用 红、绿、蓝 三种颜色为每个单元格涂色。所有单元格都需要被涂色。涂色方案需要满足：不存在相邻两个单元格颜色相同的情况 。返回网格涂色的方法数。因为答案可能非常大， 返回 对 109 + 7 取余 的结果。[1931.用三种不同颜色为网格涂色](https://leetcode.cn/problems/painting-a-grid-with-three-different-colors/description/)

- 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。[416.分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/description/)

- 存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。[847.访问所有节点的最短路径](https://leetcode.cn/problems/shortest-path-visiting-all-nodes/description/)

## 20240927

- 存在一个 无向图 ，图中有 n 个节点。其中每个节点都有一个介于 0 到 n - 1 之间的唯一编号。给你一个二维数组 graph ，其中 graph[u] 是一个节点数组，由节点 u 的邻接节点组成。形式上，对于 graph[u] 中的每个 v ，都存在一条位于节点 u 和节点 v 之间的无向边。该无向图同时具有以下属性：不存在自环（graph[u] 不包含 u）。不存在平行边（graph[u] 不包含重复值）。如果 v 在 graph[u] 内，那么 u 也应该在 graph[v] 内（该图是无向图）这个图可能不是连通图，也就是说两个节点 u 和 v 之间可能不存在一条连通彼此的路径。二分图 定义：如果能将一个图的节点集合分割成两个独立的子集 A 和 B ，并使图中的每一条边的两个节点一个来自 A 集合，一个来自 B 集合，就将这个图称为 二分图 。如果图是二分图，返回 true ；否则，返回 false 。[785.判断二分图](https://leetcode.cn/problems/is-graph-bipartite/description/)

- 给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和  bi的人归入同一组。当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。[886.可能的二分法](https://leetcode.cn/problems/possible-bipartition/description/)

- 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：值 0 代表空单元格；值 1 代表新鲜橘子；值 2 代表腐烂的橘子。每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。[994.腐烂的橘子](https://leetcode.cn/problems/rotting-oranges/description/)

## 20241009

- 给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。[491.非递减子序列](https://leetcode.cn/problems/non-decreasing-subsequences/description/)

- 给你一个按 非递减顺序 排列的整数数组 nums 。请你判断是否能在将 nums 分割成 一个或多个子序列 的同时满足下述 两个 条件：每个子序列都是一个 连续递增序列（即，每个整数 恰好 比前一个整数大 1 ）。所有子序列的长度 至少 为 3 。如果可以分割 nums 并满足上述条件，则返回 true ；否则，返回 false 。[659.分割数组为连续子序列](https://leetcode.cn/problems/split-array-into-consecutive-subsequences/description/)

- 一个 2D 网格中的 峰值 是指那些 严格大于 其相邻格子(上、下、左、右)的元素。给你一个 从 0 开始编号 的 m x n 矩阵 mat ，其中任意两个相邻格子的值都 不相同 。找出 任意一个 峰值 mat[i][j] 并 返回其位置 [i,j] 。你可以假设整个矩阵周边环绕着一圈值为 -1 的格子。要求必须写出时间复杂度为 O(m log(n)) 或 O(n log(m)) 的算法。[1901.寻找峰值II](https://leetcode.cn/problems/find-a-peak-element-ii/description/)

- 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。两个相邻元素间的距离为 1 。[542.01矩阵](https://leetcode.cn/problems/01-matrix/description/)

- 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。你可以对一个单词进行如下三种操作：插入一个字符，删除一个字符，替换一个字符。[72.编辑距离](https://leetcode.cn/problems/edit-distance/description/)

- 给你一个整数 n ，表示有 n 节课，课程编号从 1 到 n 。同时给你一个二维整数数组 relations ，其中 relations[j] = [prevCoursej, nextCoursej] ，表示课程 prevCoursej 必须在课程 nextCoursej 之前 完成（先修课的关系）。同时给你一个下标从 0 开始的整数数组 time ，其中 time[i] 表示完成第 (i+1) 门课程需要花费的 月份 数。请你根据以下规则算出完成所有课程所需要的 最少 月份数：如果一门课的所有先修课都已经完成，你可以在 任意 时间开始这门课程。你可以 同时 上 任意门课程 。
请你返回完成所有课程所需要的 最少 月份数。注意：测试数据保证一定可以完成所有课程（也就是先修课的关系构成一个有向无环图）。[2050.并行课程III](https://leetcode.cn/problems/parallel-courses-iii/description/)

- 有 n 个项目，每个项目或者不属于任何小组，或者属于 m 个小组之一。group[i] 表示第 i 个项目所属的小组，如果第 i 个项目不属于任何小组，则 group[i] 等于 -1。项目和小组都是从零开始编号的。可能存在小组不负责任何项目，即没有任何项目属于这个小组。请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：同一小组的项目，排序后在列表中彼此相邻。项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前（位于第 i 个项目左侧）应该完成的所有项目。如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 空列表 。[1203.项目管理](https://leetcode.cn/problems/sort-items-by-groups-respecting-dependencies/description/)

## 20241012

- 给你一棵二叉树的根节点 root ，返回所有 重复的子树 。对于同一类的重复子树，你只需要返回其中任意 一棵 的根结点即可。如果两棵树具有 相同的结构 和 相同的结点值 ，则认为二者是 重复 的。[652.寻找重复的子树](https://leetcode.cn/problems/find-duplicate-subtrees/description/)

- 给你一个目录信息列表 paths ，包括目录路径，以及该目录中的所有文件及其内容，请你按路径返回文件系统中的所有重复文件。答案可按 任意顺序 返回。一组重复的文件至少包括 两个 具有完全相同内容的文件。输入 列表中的单个目录信息字符串的格式如下："root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)" 这意味着，在目录 root/d1/d2/.../dm 下，有 n 个文件 ( f1.txt, f2.txt ... fn.txt ) 的内容分别是 ( f1_content, f2_content ... fn_content ) 。注意：n >= 1 且 m >= 0 。如果 m = 0 ，则表示该目录是根目录。输出 是由 重复文件路径组 构成的列表。其中每个组由所有具有相同内容文件的文件路径组成。文件路径是具有下列格式的字符串："directory_path/file_name.txt" [609.在系统中查找重复文件](https://leetcode.cn/problems/find-duplicate-file-in-system/description/)

- 有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。[787.K站中转内最便宜的航班](https://leetcode.cn/problems/cheapest-flights-within-k-stops/description/)

## 20241016

- 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，两者长度都为 n 。每次操作中，你可以选择交换 nums1 中任意两个下标处的值。操作的 开销 为两个下标的 和 。你的目标是对于所有的 0 <= i <= n - 1 ，都满足 nums1[i] != nums2[i] ，你可以进行 任意次 操作，请你返回达到这个目标的 最小 总代价。请你返回让 nums1 和 nums2 满足上述条件的 最小总代价 ，如果无法达成目标，返回 -1 。[2499.让数组不相等的最小总代价](https://leetcode.cn/problems/minimum-total-cost-to-make-arrays-unequal/description/)

- 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，两者长度都是 n ，再给你一个正整数 k 。你必须从 nums1 中选一个长度为 k 的 子序列 对应的下标。对于选择的下标 i0 ，i1 ，...， ik - 1 ，你的 分数 定义如下：nums1 中下标对应元素求和，乘以 nums2 中下标对应元素的 最小值 。用公式表示： (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]) 。
请你返回 最大 可能的分数。一个数组的 子序列 下标是集合 {0, 1, ..., n-1} 中删除若干元素得到的剩余集合，也可以不删除任何元素。[2542.最大子序列的分数](https://leetcode.cn/problems/maximum-subsequence-score/description/)

- 设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，不是第 k 个不同的元素。请实现 KthLargest 类：KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。[703.数据流中的第K大元素](https://leetcode.cn/problems/kth-largest-element-in-a-stream/description/)

- 给定两个整数 n 和 k，以及两个长度为 n 的整数数组 speed 和 efficiency。现有 n 名工程师，编号从 1 到 n。其中 speed[i] 和 efficiency[i] 分别代表第 i 位工程师的速度和效率。从这 n 名工程师中最多选择 k 名不同的工程师，使其组成的团队具有最大的团队表现值。团队表现值 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。请你返回该团队的​​​​​​最大团队表现值，由于答案可能很大，请你返回结果对 10^9 + 7 取余后的结果。[1383.最大的团队表现值](https://leetcode.cn/problems/maximum-performance-of-a-team/description/)

- 几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。你的点数就是你拿到手中的所有卡牌的点数之和。给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。[1423.可获得的最大点数](https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/description/)

- 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。[108.将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/)

- 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。[938.二叉搜索树的范围和](https://leetcode.cn/problems/range-sum-of-bst/description/)


- 给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：() 得 1 分。AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。(A) 得 2 * A 分，其中 A 是平衡括号字符串。[856.括号的分数](https://leetcode.cn/problems/score-of-parentheses/description/)

## 20241023

- 给你一个二叉树的根节点 root ，计算并返回 整个树 的坡度 。一个树的 节点的坡度 定义即为，该节点左子树的节点之和和右子树节点之和的 差的绝对值 。如果没有左子树的话，左子树的节点之和为 0 ；没有右子树的话也是一样。空结点的坡度是 0 。整个树 的坡度就是其所有节点的坡度之和。[563.二叉树的坡度](https://leetcode.cn/problems/binary-tree-tilt/description/)

- 给你一棵 n 个节点的树，编号从 0 到 n - 1 ，以父节点数组 parent 的形式给出，其中 parent[i] 是第 i 个节点的父节点。树的根节点为 0 号节点，所以 parent[0] = -1 ，因为它没有父节点。你想要设计一个数据结构实现树里面对节点的加锁，解锁和升级操作。数据结构需要支持如下函数：
Lock：指定用户给指定节点 上锁 ，上锁后其他用户将无法给同一节点上锁。只有当节点处于未上锁的状态下，才能进行上锁操作。Unlock：指定用户给指定节点 解锁 ，只有当指定节点当前正被指定用户锁住时，才能执行该解锁操作。Upgrade：指定用户给指定节点 上锁 ，并且将该节点的所有子孙节点 解锁 。只有如下 3 个条件 全部 满足时才能执行升级操作：指定节点当前状态为未上锁。指定节点至少有一个上锁状态的子孙节点（可以是 任意 用户上锁的）。指定节点没有任何上锁的祖先节点。请你实现 LockingTree 类：
LockingTree(int[] parent) 用父节点数组初始化数据结构。lock(int num, int user) 如果 id 为 user 的用户可以给节点 num 上锁，那么返回 true ，否则返回 false 。如果可以执行此操作，节点 num 会被 id 为 user 的用户 上锁 。unlock(int num, int user) 如果 id 为 user 的用户可以给节点 num 解锁，那么返回 true ，否则返回 false 。如果可以执行此操作，节点 num 变为 未上锁 状态。upgrade(int num, int user) 如果 id 为 user 的用户可以给节点 num 升级，那么返回 true ，否则返回 false 。如果可以执行此操作，节点 num 会被 升级 。[1993.树上的操作](https://leetcode.cn/problems/operations-on-tree/description/)

- 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。[300.最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/description/)

- 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表，用字母 A 到 Z 表示，以及一个冷却时间 n。每个周期或时间间隔允许完成一项任务。任务可以按任何顺序完成，但有一个限制：两个 相同种类 的任务之间必须有长度为 n 的冷却时间。返回完成所有任务所需要的 最短时间间隔 。[621.任务调度器](https://leetcode.cn/problems/task-scheduler/description/)

- 给定一个二叉树，我们在树的节点上安装摄像头。节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。计算监控树的所有节点所需的最小摄像头数量。[968.监控二叉树](https://leetcode.cn/problems/binary-tree-cameras/description/)

- 给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。
```bash
class Node {
    public int val;
    public List<Node> neighbors;
}
```
测试用例格式：简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。[133.克隆图](https://leetcode.cn/problems/clone-graph/description/)

- 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。[207.课程表](https://leetcode.cn/problems/course-schedule/description/)

## 20241030

- 给定一个非负整数数组 nums 和一个整数 k ，你需要将这个数组分成 k 个非空的连续子数组，使得这 k 个子数组各自和的最大值 最小。返回分割后最小的和的最大值。子数组 是数组中连续的部份。[410.分割数组的最大值](https://leetcode.cn/problems/split-array-largest-sum/description/)

- 珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。[875.爱吃香蕉的珂珂](https://leetcode.cn/problems/koko-eating-bananas/description/)

- 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。返回 滑动窗口中的最大值 。[239.滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/description/)

- 给定两个长度相等的数组 nums1 和 nums2，nums1 相对于 nums2 的优势可以用满足 nums1[i] > nums2[i] 的索引 i 的数目来描述。返回 nums1 的 任意 排列，使其相对于 nums2 的优势最大化。[870.优势洗牌](https://leetcode.cn/problems/advantage-shuffle/description/)


- 我们将整数 x 的 权重 定义为按照下述规则将 x 变成 1 所需要的步数：如果 x 是偶数，那么 x = x / 2. 如果 x 是奇数，那么 x = 3 * x + 1。比方说，x=3 的权重为 7 。因为 3 需要 7 步变成 1 （3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）。给你三个整数 lo， hi 和 k 。你的任务是将区间 [lo, hi] 之间的整数按照它们的权重 升序排序 ，如果大于等于 2 个整数有 相同 的权重，那么按照数字自身的数值 升序排序 。请你返回区间 [lo, hi] 之间的整数按权重排序后的第 k 个数。注意，题目保证对于任意整数 x （lo <= x <= hi） ，它变成 1 所需要的步数是一个 32 位有符号整数。[1387.将整数按权重排序](https://leetcode.cn/problems/sort-integers-by-the-power-value/description/)

## 20241106

- 树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，任何一个没有简单环路的连通图都是一棵树。给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。[310.最小高度树](https://leetcode.cn/problems/minimum-height-trees/description/)

- 如果一个二进制字符串，是以一些 0（可能没有 0）后面跟着一些 1（也可能没有 1）的形式组成的，那么该字符串是 单调递增 的。给你一个二进制字符串 s，你可以将任何 0 翻转为 1 或者将 1 翻转为 0 。返回使 s 单调递增的最小翻转次数。[926.将字符串翻转到单调递增](https://leetcode.cn/problems/flip-string-to-monotone-increasing/description/)

- 给定一个经过编码的字符串，返回它解码后的字符串。编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。[394.字符串解码](https://leetcode.cn/problems/decode-string/description/)

- 给定一个编码字符串 s 。请你找出 解码字符串 并将其写入磁带。解码时，从编码字符串中 每次读取一个字符 ，并采取以下步骤：如果所读的字符是字母，则将该字母写在磁带上。如果所读的字符是数字（例如 d），则整个当前磁带总共会被重复写 d-1 次。现在，对于给定的编码字符串 s 和索引 k，查找并返回解码字符串中的第 k 个字母。[880.索引处的解码字符串](https://leetcode.cn/problems/decoded-string-at-index/description/)

## 20241113

- 给你一个 n x n 的网格 grid ，代表一块樱桃地，每个格子由以下三种数字的一种来表示：0 表示这个格子是空的，所以你可以穿过它。1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。-1 表示这个格子里有荆棘，挡着你的路。请你统计并返回：在遵守下列规则的情况下，能摘到的最多樱桃数：从位置 (0, 0) 出发，最后到达 (n - 1, n - 1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为 0 或者 1 的格子）；当到达 (n - 1, n - 1) 后，你要继续走，直到返回到 (0, 0) ，只能向上或向左走，并且只能穿越有效的格子；当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为 0 ）；如果在 (0, 0) 和 (n - 1, n - 1) 之间不存在一条可经过的路径，则无法摘到任何一个樱桃。[741.摘樱桃](https://leetcode.cn/problems/cherry-pickup/description/)


- 给你一个 rows x cols 的矩阵 grid 来表示一块樱桃地。 grid 中每个格子的数字表示你能获得的樱桃数目。你有两个机器人帮你收集樱桃，机器人 1 从左上角格子 (0,0) 出发，机器人 2 从右上角格子 (0, cols-1) 出发。请你按照如下规则，返回两个机器人能收集的最多樱桃数目：从格子 (i,j) 出发，机器人可以移动到格子 (i+1, j-1)，(i+1, j) 或者 (i+1, j+1) 。当一个机器人经过某个格子时，它会把该格子内所有的樱桃都摘走，然后这个位置会变成空格子，即没有樱桃的格子。当两个机器人同时到达同一个格子时，它们中只有一个可以摘到樱桃。两个机器人在任意时刻都不能移动到 grid 外面。两个机器人最后都要到达 grid 最底下一行。[1463.摘樱桃II](https://leetcode.cn/problems/cherry-pickup-ii/description/)

- 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。说明：每次只能向下或者向右移动一步。[64.最小路径和](https://leetcode.cn/problems/minimum-path-sum/description/)

- 给定两个数组 nums1 和 nums2 ，返回 它们的 交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。[349.两个数组的交集](https://leetcode.cn/problems/intersection-of-two-arrays/description/)


- 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。[56.合并区间](https://leetcode.cn/problems/merge-intervals/description/)


- 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。[51.N皇后](https://leetcode.cn/problems/n-queens/description/)

- n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。[52.N皇后II](https://leetcode.cn/problems/n-queens-ii/description/)

- 编写一个程序，通过填充空格来解决数独问题。数独的解法需 遵循如下规则：数字 1-9 在每一行只能出现一次。数字 1-9 在每一列只能出现一次。数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）数独部分空格内已填入了数字，空白格用 '.' 表示。[37.解数独](https://leetcode.cn/problems/sudoku-solver/description/)

- 请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。数字 1-9 在每一行只能出现一次。数字 1-9 在每一列只能出现一次。数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）注意：一个有效的数独（部分已被填充）不一定是可解的。只需要根据以上规则，验证已经填入的数字是否有效即可。空白格用 '.' 表示。[36.有效的数独](https://leetcode.cn/problems/valid-sudoku/description/)


- 「推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库中的目标位置。游戏地图用大小为 m x n 的网格 grid 表示，其中每个元素可以是墙、地板或者是箱子。现在你将作为玩家参与游戏，按规则将箱子 'B' 移动到目标位置 'T' ：玩家用字符 'S' 表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。地板用字符 '.' 表示，意味着可以自由行走。墙用字符 '#' 表示，意味着障碍物，不能通行。 箱子仅有一个，用字符 'B' 表示。相应地，网格上有一个目标位置 'T'。玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。玩家无法越过箱子。返回将箱子推到目标位置的最小 推动 次数，如果无法做到，请返回 -1。[1263.推箱子](https://leetcode.cn/problems/minimum-moves-to-move-a-box-to-their-target-location/description/)


## 20241120

- 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。说明：每次只能向下或者向右移动一步。[64.最小路径和](https://leetcode.cn/problems/minimum-path-sum/description/)

- 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:0 <= j <= nums[i] i + j < n。返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。[45.跳跃游戏II](https://leetcode.cn/problems/jump-game-ii/description/)

- 给定一个字符串数组 words，找到以 words 中每个字符串作为子字符串的最短字符串。如果有多个有效最短字符串满足题目条件，返回其中 任意一个 即可。我们可以假设 words 中没有字符串是 words 中另一个字符串的子字符串。[943.最短超级串](https://leetcode.cn/problems/find-the-shortest-superstring/description/)

- 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。[207.课程表](https://leetcode.cn/problems/course-schedule/description/)

- 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。[210.课程表II](https://leetcode.cn/problems/course-schedule-ii/description/)


- 给你一个下标从 0 开始的整数数组 nums 和一个整数 k 。一开始你在下标 0 处。每一步，你最多可以往前跳 k 步，但你不能跳出数组的边界。也就是说，你可以从下标 i 跳到 [i + 1， min(n - 1, i + k)] 包含 两个端点的任意位置。你的目标是到达数组最后一个位置（下标为 n - 1 ），你的 得分 为经过的所有数字之和。请你返回你能得到的 最大得分 。[1696.跳跃游戏VI](https://leetcode.cn/problems/jump-game-vi/description/)

- 给你一个整数数组 nums 和一个整数 k ，请你返回 非空 子序列元素和的最大值，子序列需要满足：子序列中每两个 相邻 的整数 nums[i] 和 nums[j] ，它们在原数组中的下标 i 和 j 满足 i < j 且 j - i <= k 。数组的子序列定义为：将数组中的若干个数字删除（可以删除 0 个数字），剩下的数字按照原本的顺序排布。[1425.带限制的子序列和](https://leetcode.cn/problems/constrained-subsequence-sum/description/)

- 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。[279.完全平方数](https://leetcode.cn/problems/perfect-squares/description/)

## 20241127

- 给定一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点，并且是一个整数 k ，返回离原点 (0,0) 最近的 k 个点。这里，平面上两点之间的距离是 欧几里德距离（ √(x1 - x2)2 + (y1 - y2)2 ）。你可以按 任何顺序 返回答案。除了点坐标的顺序之外，答案 确保 是 唯一 的。[973.最接近原点的K个点](https://leetcode.cn/problems/k-closest-points-to-origin/description/)

- 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。[1094.拼车](https://leetcode.cn/problems/car-pooling/description/)

- 有 n 个城市通过一些航班连接。给你一个数组 flights ，其中 flights[i] = [fromi, toi, pricei] ，表示该航班都从城市 fromi 开始，以价格 pricei 抵达 toi。现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到出一条最多经过 k 站中转的路线，使得从 src 到 dst 的 价格最便宜 ，并返回该价格。 如果不存在这样的路线，则输出 -1。[787.K站中转内最便宜的航班](https://leetcode.cn/problems/cheapest-flights-within-k-stops/description/)

## 20241204

- 给定一个整数数组 asteroids，表示在同一行的小行星。数组中小行星的索引表示它们在空间中的相对位置。对于数组中的每一个元素，其绝对值表示小行星的大小，正负表示小行星的移动方向（正表示向右移动，负表示向左移动）。每一颗小行星以相同的速度移动。找出碰撞后剩下的所有小行星。碰撞规则：两个小行星相互碰撞，较小的小行星会爆炸。如果两颗小行星大小相同，则两颗小行星都会爆炸。两颗移动方向相同的小行星，永远不会发生碰撞。[735.小行星碰撞](https://leetcode.cn/problems/asteroid-collision/description/)

- 给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1 。[1293.网格中的最短路径](https://leetcode.cn/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/)

- 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。[416.分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/description/)

- 有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：如果 x == y，那么两块石头都会被完全粉碎；如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。[1049.最后一块石头的重量II](https://leetcode.cn/problems/last-stone-weight-ii/description/)

- 给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。以数组形式返回答案。[1365.有多少小于当前数字的数字](https://leetcode.cn/problems/how-many-numbers-are-smaller-than-the-current-number/description/)



## 20241211

- 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。[485.最大连续1的个数](https://leetcode.cn/problems/max-consecutive-ones/description/)

- 有一个 单线程 CPU 正在运行一个含有 n 道函数的程序。每道函数都有一个位于  0 和 n-1 之间的唯一标识符。函数调用 存储在一个 调用栈 上 ：当一个函数调用开始时，它的标识符将会推入栈中。而当一个函数调用结束时，它的标识符将会从栈中弹出。标识符位于栈顶的函数是 当前正在执行的函数 。每当一个函数开始或者结束时，将会记录一条日志，包括函数标识符、是开始还是结束、以及相应的时间戳。给你一个由日志组成的列表 logs ，其中 logs[i] 表示第 i 条日志消息，该消息是一个按 "{function_id}:{"start" | "end"}:{timestamp}" 进行格式化的字符串。例如，"0:start:3" 意味着标识符为 0 的函数调用在时间戳 3 的 起始开始执行 ；而 "1:end:2" 意味着标识符为 1 的函数调用在时间戳 2 的 末尾结束执行。注意，函数可以 调用多次，可能存在递归调用 。函数的 独占时间 定义是在这个函数在程序所有函数调用中执行时间的总和，调用其他函数花费的时间不算该函数的独占时间。例如，如果一个函数被调用两次，一次调用执行 2 单位时间，另一次调用执行 1 单位时间，那么该函数的 独占时间 为 2 + 1 = 3 。以数组形式返回每个函数的 独占时间 ，其中第 i 个下标对应的值表示标识符 i 的函数的独占时间。[636.函数的独占时间](https://leetcode.cn/problems/exclusive-time-of-functions/description/)


- 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。[416.分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/description/)

## 20241218

- 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。返回矩阵中 省份 的数量。[547.省份数量](https://leetcode.cn/problems/number-of-provinces/description/)

- 给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。[402.移除K位数字](https://leetcode.cn/problems/remove-k-digits/description/)

- 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。[316.去除重复字母](https://leetcode.cn/problems/remove-duplicate-letters/description/)

- 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。[416.分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/description/)

- 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。[474.一和零](https://leetcode.cn/problems/ones-and-zeroes/description/)

- 丑数 就是只包含质因数 2、3 和 5 的 正 整数。给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。[263.丑数](https://leetcode.cn/problems/ugly-number/description/)


- 给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和  bi的人归入同一组。当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。[886.可能的二分法](https://leetcode.cn/problems/possible-bipartition/description/)

## 20241225

- 树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，任何一个没有简单环路的连通图都是一棵树。给你一棵包含 n 个节点的树，标记为 0 到 n - 1 。给定数字 n 和一个有 n - 1 条无向边的 edges 列表（每一个边都是一对标签），其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条无向边。可选择树中任何一个节点作为根。当选择节点 x 作为根节点时，设结果树的高度为 h 。在所有可能的树中，具有最小高度的树（即，min(h)）被称为 最小高度树 。请你找到所有的 最小高度树 并按 任意顺序 返回它们的根节点标签列表。树的 高度 是指根节点和叶子节点之间最长向下路径上边的数量。[310.最小高度树](https://leetcode.cn/problems/minimum-height-trees/description/)

- 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。[79.单词搜索](https://leetcode.cn/problems/word-search/description/)

## 20240108

- 给定一个含有 n 个正整数的数组和一个正整数 target 。找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。[209.长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/description/)

- 给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和  bi的人归入同一组。当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。[886.可能的二分法](https://leetcode.cn/problems/possible-bipartition/description/)

- 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false。[207.课程表](https://leetcode.cn/problems/course-schedule/description/) 

- 有一个有 n 个节点的有向图，节点按 0 到 n - 1 编号。图由一个 索引从 0 开始 的 2D 整数数组 graph表示， graph[i]是与节点 i 相邻的节点的整数数组，这意味着从节点 i 到 graph[i]中的每个节点都有一条边。如果一个节点没有连出的有向边，则该节点是 终端节点 。如果从该节点开始的所有可能路径都通向 终端节点（或另一个安全节点），则该节点为 安全节点。返回一个由图中所有 安全节点 组成的数组作为答案。答案数组中的元素应当按 升序 排列。[802.找到最终的安全状态](https://leetcode.cn/problems/find-eventual-safe-states/description/)

## 20250115

- 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求：路径途经的所有单元格的值都是 0 。路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。畅通路径的长度 是该路径途经的单元格总数。[1091.二进制矩阵中的最短路径](https://leetcode.cn/problems/shortest-path-in-binary-matrix/description/)

- 请你将一些箱子装在 一辆卡车 上。给你一个二维数组 boxTypes ，其中 boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi] ：numberOfBoxesi 是类型 i 的箱子的数量。numberOfUnitsPerBoxi 是类型 i 每个箱子可以装载的单元数量。整数 truckSize 表示卡车上可以装载 箱子 的 最大数量 。只要箱子数量不超过 truckSize ，你就可以选择任意箱子装到卡车上。返回卡车可以装载 单元 的 最大 总数。[1710.卡车上的最大单元数](https://leetcode.cn/problems/maximum-units-on-a-truck/description/)

- 按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord -> s1 -> s2 -> ... -> sk 这样的单词序列，并满足：每对相邻的单词之间仅有单个字母不同。
转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单词。sk == endWord
给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。请你找出并返回所有从 beginWord 到 endWord 的 最短转换序列 ，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk] 的形式返回。[126.单词接龙II](https://leetcode.cn/problems/word-ladder-ii/description/)

## 20250219

- 在二维网格 grid 上，有 4 种类型的方格：1 表示起始方格。且只有一个起始方格。2 表示结束方格，且只有一个结束方格。0 表示我们可以走过的空方格。-1 表示我们无法跨越的障碍。返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目。每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格。[980.不同路径III](https://leetcode.cn/problems/unique-paths-iii/description/)

- 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近 10 条推文。实现 Twitter 类：Twitter() 初始化简易版推特对象void postTweet(int userId, int tweetId) 根据给定的 tweetId 和 userId 创建一条新推文。每次调用此函数都会使用一个不同的 tweetId 。List<Integer> getNewsFeed(int userId) 检索当前用户新闻推送中最近  10 条推文的 ID 。新闻推送中的每一项都必须是由用户关注的人或者是用户自己发布的推文。推文必须 按照时间顺序由最近到最远排序 。void follow(int followerId, int followeeId) ID 为 followerId 的用户开始关注 ID 为 followeeId 的用户。void unfollow(int followerId, int followeeId) ID 为 followerId 的用户不再关注 ID 为 followeeId 的用户。[355.设计推特](https://leetcode.cn/problems/design-twitter/description/)
