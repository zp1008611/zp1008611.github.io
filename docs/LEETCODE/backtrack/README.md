# 回溯

## Reference

- https://www.bilibili.com/video/BV1mG4y1A7Gu?spm_id_from=333.788.player.switch&vd_source=3d4b12fb4a4bfbc98942d43612ae2fb9
- https://leetcode.cn/discuss/post/3142882/fen-xiang-gun-ti-dan-lian-biao-er-cha-sh-6srp/

## 二叉树上的回溯

1. 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径. 叶子节点是指没有子节点的节点. 

2. 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径. 叶子节点 是指没有子节点的节点. 

3. 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目. 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）. 

    ```python
    # 定义二叉树节点类
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # 问题1：返回所有从根节点到叶子节点的路径
    def binaryTreePaths(root):
        paths = []
        def dfs(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    path += "->"
                    dfs(node.left, path)
                    dfs(node.right, path)
        dfs(root, "")
        return paths

    # 问题2：找出所有从根节点到叶子节点路径总和等于给定目标和的路径
    def pathSumII(root, targetSum):
        result = []
        def dfs(node, path, current_sum):
            if node:
                current_sum += node.val
                path = path + [node.val]
                if not node.left and not node.right and current_sum == targetSum:
                    result.append(path)
                dfs(node.left, path.copy(), current_sum)
                dfs(node.right, path.copy(), current_sum)
        dfs(root, [], 0)
        return result

    # 问题3：求该二叉树里节点值之和等于targetSum的路径的数目
    def pathSumIII(root, targetSum):
        def count_paths_from_node(node, target):
            if not node:
                return 0
            count = 0
            if node.val == target:
                count += 1
            count += count_paths_from_node(node.left, target - node.val)
            count += count_paths_from_node(node.right, target - node.val)
            return count

        if not root:
            return 0
        return count_paths_from_node(root, targetSum) + pathSumIII(root.left, targetSum) + pathSumIII(root.right, targetSum)
    ```


## 子集型回溯

1. 给你一个整数数组 nums ，数组中的元素 互不相同 . 返回该数组所有可能的子集（幂集）. 解集 不能 包含重复的子集. 你可以按 任意顺序 返回解集. 

    ```python
    def subsets(nums):
        result = []
        def backtrack(start, path):
            # 每次递归都将当前子集加入结果集
            result.append(path[:])
            for i in range(start, len(nums)):
                # 选择当前元素
                path.append(nums[i])
                # 递归处理剩余元素
                backtrack(i + 1, path)
                # 回溯，撤销选择
                path.pop()
        backtrack(0, [])
        return result
    ```

## 组合型回溯

1. 从 n 个不同元素中取出 k 个元素的所有组合

    ```python
    def combine(n, k):
        result = []
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        backtrack(1, [])
        return result
    ```

## 排列型回溯

1. 求解数字数组的所有排列

    ```python
    def permute(nums):
        result = []
        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(path, used)
                path.pop()
                used[i] = False
        used = [False] * len(nums)
        backtrack([], used)
        return result
    ```

## 划分型回溯

1. 给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 . 返回 s 所有可能的分割方案. 

    ```python
    def partition(s):
        result = []
        def is_palindrome(sub):
            return sub == sub[::-1]
        def backtrack(start, path):
            if start == len(s):
                # 当遍历完字符串时，将当前分割方案加入结果集
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if is_palindrome(sub):
                    # 如果当前子串是回文串，则选择该子串
                    path.append(sub)
                    # 递归处理剩余字符串
                    backtrack(end, path)
                    # 回溯，撤销选择
                    path.pop()
        backtrack(0, [])
        return result
    ```