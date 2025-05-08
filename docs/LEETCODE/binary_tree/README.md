# 二叉树

## Reference

- https://leetcode.cn/discuss/post/3142882/fen-xiang-gun-ti-dan-lian-biao-er-cha-sh-6srp/


## 遍历二叉树

1. 给你二叉树的根节点 root ，返回它节点值的 前序 遍历 [LC144](https://leetcode.cn/problems/binary-tree-preorder-traversal/description/)

    - 前序遍历的顺序为：根节点 -> 左子树 -> 右子树
    - 用栈存储节点，先将根节点入栈，每次弹出栈顶节点访问，再依次将右、左子节点入栈

2. 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 [LC94](https://leetcode.cn/problems/binary-tree-inorder-traversal/description/)

    - 中序遍历的顺序为：左子树 -> 根节点 -> 右子树
    - 用栈模拟递归，从根节点开始不断将左子节点入栈，直到为空，弹出节点访问，再处理其右子树

3. 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 [LC145](https://leetcode.cn/problems/binary-tree-postorder-traversal/description/)

    - 后序遍历的顺序为：左子树 -> 右子树 -> 根节点。
    - 用两个栈，先将根节点入第一个栈，弹出后入第二个栈，再将其左右子节点入第一个栈，最后依次弹出第二个栈节点

4. 请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 . 如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的. 如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false . [LC872](https://leetcode.cn/problems/leaf-similar-trees/description/) 

    - 分别用深度优先搜索遍历两棵树，记录叶子节点值形成序列，比较两个序列是否相同

5. 给定二叉树的根节点 root ，返回所有左叶子之和 [LC404](https://leetcode.cn/problems/sum-of-left-leaves/description/)

    - 用深度优先搜索遍历树，传递节点是否为左子节点的标志，若为左叶子节点则累加其值

## 二叉树DFS递归


### 在“递”的过程中维护值

1. 给定一个二叉树 root ，返回其最大深度。二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。[LC104](https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/)

    - 递归遍历左右子树，“递” 时深度加 1，“归” 时取左右子树深度最大值再加 1 为当前节点深度，空节点深度为 0。

2. 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。叶子节点 是指没有子节点的节点。[LC112](https://leetcode.cn/problems/path-sum/description/)

    - “递” 时用目标和减去当前节点值，到叶子节点时判断剩余目标和是否等于节点值，左右子树有一个满足则为 True。

3. 给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。计算从根节点到叶节点生成的 所有数字之和 。 [LC129](https://leetcode.cn/problems/sum-root-to-leaf-numbers/description/)

    - “递” 时将已形成数字乘 10 加当前节点值，到叶子节点累加该数字，遍历完所有路径得总和。


4. 给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。好节点X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。[LC1448](https://leetcode.cn/problems/count-good-nodes-in-binary-tree/description/)

    - “递” 时维护路径最大值，节点值大于等于该值则为好节点，计数器加 1 并更新最大值，继续遍历子树。

### 在“归”的过程中维护值

1. 如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。只有给定的树是单值二叉树时，才返回 true；否则返回 false。[LC965](https://leetcode.cn/problems/univalued-binary-tree/description/)

    - 递归检查左右子树是否单值，“归” 时若左右子树单值且节点值相同则当前子树单值。空节点默认单值。

2. 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。[LC100](https://leetcode.cn/problems/same-tree/description/)

    - 递归检查左右子树是否相同，“归” 时若左右子树相同且当前节点值相等则两树相同。节点一有一空就不同

3. 给你一个二叉树的根节点 root ， 检查它是否轴对称 [LC101](https://leetcode.cn/problems/symmetric-tree/description/)

    - 递归检查左左与右右、左右与右左是否对称，“归” 时若对称且根节点值相等则树对称。节点一有一空就不对称。

4. 给定二叉树的根节点 root，找出存在于 不同 节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。（如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）[LC1026](https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/description/)

    - 递归维护路径最大最小值，“归” 时计算当前节点与最值差值，取左右子树最大差值。

## 二叉树BFS

## 创建二叉树

1. 

## 直径

## 最近公共祖先

## 二叉搜索树