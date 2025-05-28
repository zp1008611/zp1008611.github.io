# LEETCODE HOT150

## Reference

- https://leetcode.cn/studyplan/top-interview-150/
- https://leetcode.cn/studyplan/top-100-liked/

## 双指针

> 如果是原地修改，用快慢指针，慢指针用于写，快指针用于读

1. 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。[LC88](合并两个有序数组)(https://leetcode.cn/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)


同向指针，从右边往左边

```python
for i in range(m,m+n):
        nums1[i] = nums2[i-m]
    # 不能用sort(nums1)，这个方法是返回一个新的数组
    nums1.sort()
```
    - 如果不用sort方法呢？
    - 两个数组都是非递减的，那么可以从尾巴开始比较，i=m-1,j=n-1,p=m+n-1
    - 如果nums1[i]>nums2[j]，那么把nums[i]放到p的位置，i--,j不动，p--，循环比较，直到p<0,i<0,j<0
    - 注意如果i<0，就是nums1的数已经比较完了，直接把nums2的数把空位补好，如果j<0，同理
    - while循环判断p>=0，依次判断i<0 and j>=0，j<0 and i<=0 ,i<=0 and j<=0, i>=0,j>=0的情况.

2. 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。返回 k。[LC27移除元素](https://leetcode.cn/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150)

同向指针，快慢指针，慢指针用于写，快指针用于读

    - 慢指针i=0，快指针j=0，i用于写，j用于读，k=0记录
    - 如果nums[j]==val，不需要写，故i不动，j++，如果nums[j]!=val，需要写，故nums[i]=nums[j]，i++,j++,k++
    - 可见j一直要加所以，可以用for循环

3. 给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。[LC26删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)

    - 慢指针i=1，快指针j=1，i用于写，j用于读，k=1记录，val用于记录前一个访问的数
    - 如果nums[j]==val，不需要写，故i不动，j++，如果nums[j]!=val，需要写，故nums[i]=nums[j]，i++,j++,k++,val=nums[j]
    - 可见j一直要加所以，可以用for循环
    - 注意这里val要存一个值，先存nums[0]，所以第一个数就不动了，故i，j，k从1开始
    - 这里可以不特判，如果数组长度为1，那么直接返回k=1

4. 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。[LC80删除有序数组中的重复项II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150)

    - 慢指针i=2，快指针j=2，i用于写，j用于读，val用于记录前一个访问的数，valn记录是否和val相对次数为2
    - 如果nums[j]==val且valn>=2，不需要写，故i不动，j++,valn++，如果nums[j]==val且valn<2，需要写，故i++，j++,valn++，如果nums[j]!=val，需要写，故nums[i]=nums[j]，i++,j++,val=nums[j],valn=1
    - 可见j一直要加所以，可以用for循环
    - 注意这里前两个数可以直接不动了，故i，j从2开始
    - i最后写完的位置是新数组的最后一个下标+1，故返回i
    - 注意这里要特判，因为我们的指针从2开始，如果数组长度小于等于2的数组，直接返回数组长度·


## 数学

5. 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。[LC189轮转数组](https://leetcode.cn/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150)

    - 每个下标i轮转k之后得到得新下标为 (i+k)%len(nums)
    - 0+3->3,6+3%7->2
    - 注意要先用一个temp数组储存nums原来的数
    - 特判: k=0时，i%len(nums)=i，没错，len(nums)=1是，假设k=3，(0+3)%1 = 0，没错
    

## 滑动窗口

## 哈希

前缀和与哈希表

双指针与哈希表

滑窗与哈希表



## 动态规划

## 回溯

> 入栈的是(下一个处理的索引a，暂时结果)，循环：（出栈，先看暂时结果是否满足输出结果条件，不满足的话，则处理索引a对应的信息加入到暂时结果中，再将(下一个处理的索引b，暂时结果)入栈. 类似DFS把邻居存入栈

1. 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。[LC17电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-interview-150)

    - 回溯，这里索引对应一个字符串
    - 初始化一个栈 stack = [(0,[])]
    - 循环：出栈，如果暂时结果满足结果条件(暂时结果数组长度==规定数组长度)，存入结果，并循环跳到下一个出栈元素，否则得到索引所有对应的值，分别加入暂时结果中，将(下一个索引，暂时结果)存入栈.


2. 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。你可以按 任何顺序 返回答案。[LC77组合](https://leetcode.cn/problems/combinations/description/?envType=study-plan-v2&envId=top-interview-150)

    

3. 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。[LC46全排列](https://leetcode.cn/problems/permutations/description/?envType=study-plan-v2&envId=top-interview-150)


4. 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。[LC78子集](https://leetcode.cn/problems/subsets/description/?envType=study-plan-v2&envId=top-100-liked)


## 图

### DFS

1. 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。此外，你可以假设该网格的四条边均被水包围。

    - 网格图 grid ,m = len(grid), n = len(grid[0]), (x,y) ，x:0-n, y:0-m
    - 遍历grid[i][j]，如果grid[i][j]=='1'，那么做DFS，上下左右方向为'1'的才能做邻居
    - DFS断了，就算一个陆地

2. 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。在选修某些课程之前需要一些先修课程。 先修课程按数组prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

    - DFS找环

### BFS

1. 

## 二叉树

### 遍历

1. 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。[LC94 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/description/?envType=study-plan-v2&envId=top-100-liked)

    - 找来一个result=[]存结果
    - 中序，根在中间，result.append(node.val)在中间


2. 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。[LC102二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/description/?envType=study-plan-v2&envId=top-100-liked)

    - BFS遍历
    - 但是这里不同的是，每一层要单独放在一个列表
    - 根节点入队列，队列非空循环：（我们希望每次while循环时此时队列的节点就是同一层的），对于目前队列的节点进行for遍历，使用一个新列表vals存储值，然后节点的左右节点入队列（新进的节点不会影响for循环），for循环完毕后，同一层的节点遍历完成，将vals存入result数组中.
    - 注意要对空root进行特判

### 前序遍历维护值

2. 给定一个二叉树 root ，返回其最大深度。二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。[LC104二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150)


    - 到一个新的根节点，子树的深度就可以+1
    - 所以用前序遍历，到新的根节点，就可以将目前的深度和最大深度ans做比较
    - 注意ans在递归函数里面，要做`nonlocal ans`说明

3. 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。[LC100相同的树](https://leetcode.cn/problems/same-tree/description/?envType=study-plan-v2&envId=top-interview-150)
 
    - 找来一个flag做标记
    - 同时做前序遍历，判断节点值是否相等，如果都不为空且不相等的话，flag=False，然后return，都为空的话，flag = True and flag，然后return，都不为空写在最下面，判断是否相等，然后接着遍历都不为空节点的左子树和右子树.

4. 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。[LC226翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked)

    - 前序遍历，到根节点后，把左子节点和右子节点互换

5. 给你一个二叉树的根节点 root ， 检查它是否轴对称。[LC101对称二叉树](https://leetcode.cn/problems/symmetric-tree/?envType=study-plan-v2&envId=top-100-liked)

    - 前序遍历，判断子树1的右子树和子树2的左子树是否相等

6. 给你一棵二叉树的根节点，返回该树的 直径 。二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。两节点之间路径的 长度 由它们之间边数表示。[LC543二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked)

    - 前序遍历，节点的直径是左子树的最大深度+右子树的最大深度，递归函数返回该节点的最大深度
    - 注意这里直径的计算不一定经过根节点

### 数组 -> 二叉树

1. 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。[LC105从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150)

    - preorder = [3,9,20,15,7]
    - inorder = [9,3,15,20,7]
    - 前序是 根->左->右，中序是 左->根->右，那么可以知道preorder[0]=3就是根结点，然后在inorder中找到3的位置，那么在inorder中3的左边的数的长度左子树的大小，3的右边的数的长度就是右子树的大小，然后根据大小可以在preorder中得到左右子树对应的数组值，接着再继续在preorder中子树的根，在inorder中找子树的子树的大小，再回到preorder找子树的子树对应的数组值
    - 递归处理

2. 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。[LC106从中序到后序遍历序列构造二叉树]

    -   inorder = [9,3,15,20,7], 
    - postorder = [9,15,7,20,3]
    - 后序是 左->右->根，中序是 左->根->右，因此postorder[-1]=3就是根节点，找到3在inorder中的位置，左边的数组就是左子树对应数组，记录数组大小left_len，右边的数组就是右子树对应数组，记录数组大小right_len，那么对应到postorder，postorder[-1:-1-right_len-1:-1]就是右子树的postorder，postorder[-1-right_len-1::-1]就是左子树的postorder，然后在找到两个子树的根节点，回到子树的inorder中再次寻找左右子树，递归


3. 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。（平衡二叉树 是指该树所有节点的左右子树的高度相差不超过 1。）[LC108将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/?envType=study-plan-v2&envId=top-100-liked)

    - 将数组看成是树的中序遍历，只要树的根节点一直在数组中间的位置，那么左右子树的高度相差不会超过1




## 栈

1. 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。有效字符串需满足：左括号必须用相同类型的右括号闭合。左括号必须以正确的顺序闭合。每个右括号都有一个对应的相同类型的左括号。[LC20
有效的括号](https://leetcode.cn/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150)

    - 匹配对(a,b)相消，入栈的只能是第一个匹配点a，匹配点b用于判断匹配
    - 找来一个栈,flag记录是否合法
    - 注意只有左括号可以入栈，所以用一个字典维护左括号和右括号的对应关系
    - 首先判断s[i]是不是左括号，如果是就入栈，如果不是左括号那么就是右括号，如果字符串合法，那么这个右括号一定与栈顶的左括号匹配，如果不匹配，那么这个字符串非法，如果最后栈非空，那么字符串也是非法的
    - 特判：len(s)==1，且s[0]为左括号入栈后就跳出，非空为False，没错，如果s[0]为右括号，直接返回false

2. 给你一个字符串 path ，表示指向某一文件或目录的 Unix 风格 绝对路径 （以 '/' 开头），请你将其转化为 更加简洁的规范路径。在 Unix 风格的文件系统中规则如下：一个点 '.' 表示当前目录本身。此外，两个点 '..' 表示将目录切换到上一级（指向父目录）。任意多个连续的斜杠（即，'//' 或 '///'）都被视为单个斜杠 '/'。任何其他格式的点（例如，'...' 或 '....'）均被视为有效的文件/目录名称。返回的 简化路径 必须遵循下述格式：始终以斜杠 '/' 开头。两个目录名之间必须只有一个斜杠 '/' 。最后一个目录名（如果存在）不能 以 '/' 结尾。此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 '.' 或 '..'）。返回简化后得到的 规范路径 。[LC71简化路径](https://leetcode.cn/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150)

    - 找来一个栈，
    - path = "/.../a/../b/c/../d/./"
    - ...入栈，a入栈，看到..，a出栈，b入栈，c入栈，看到..，c出栈，d入栈，.不用动
    - 依次出栈，然后字符串往左边加文件名和'/'
        - /.../b/d'
    - 一些处理，字符串以'/'进行分割，对于'//'的情况，会出现空字符串，看到空字符串，直接跳过
    - 如果第一个文件名就是'..'，空stack出栈会报错，所以要加一个判断
    - 特判：如果字符串长度为1，那么就只有'/'，直接返回

3. 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。实现 MinStack 类:MinStack() 初始化堆栈对象。void push(int val) 将元素val推入堆栈。void pop() 删除堆栈顶部的元素。int top() 获取堆栈顶部的元素。int getMin() 获取堆栈中的最小元素。[LC155最小栈](https://leetcode.cn/problems/min-stack/description/?envType=study-plan-v2&envId=top-interview-150)

    - 

4. 给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。请你计算该表达式。返回一个表示表达式值的整数。注意：有效的算符为 '+'、'-'、'*' 和 '/' 。每个操作数（运算对象）都可以是一个整数或者另一个表达式。两个整数之间的除法总是 向零截断 。表达式中不含除零运算。输入是一个根据逆波兰表示法表示的算术表达式。答案及所有中间计算结果可以用 32 位 整数表示。[LC150逆波兰表达式求值](https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/?envType=study-plan-v2&envId=top-interview-150)


## 单调栈
    
## 堆


2. 给定两个以 非递减顺序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。

    - 找来一个最小堆 heap=[]
    - 由于nums1和nums2非递减，所以对于(nums1[i],nums2[j])，大小顺序一定为 nums1[i]+num2[j] < nums1[i+1]+nums2[j] or nums1[i]+nums2[j+1] < nums1[i+1][j+1]
    - (i,j)出堆，那么下一个入堆的数对，从(i+1,j)或(i,j+1)选即可
    - 注意，(0,0)出堆，然后(1,0),(0,1)入堆，然后(1,1)可以由(1,0)后入堆，也可以由(0,1)后入堆，那么(1,1)就入重复了，因此只要要判断是否重复入
    - 出堆的元素数量到达k即可结束出堆.
    - 如果数量关系满足 (i,j)对应< (i,j+1)对应or (i,j+1)对应< (i,j)对应，方法：result数组长度小于k时，(i,j)出堆并存入result，如果(i+1,j)有效且没有访问过，入堆；如果(i,j+1)有效且没有访问过，入堆，当result数组长度大于k，则退出循环，result的末尾就是第k小

1. 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。[LC215数组中的第k个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=top-interview-150)

    - 固定长度的堆，遍历元素入堆，当堆的长度大于k，则最小值出堆