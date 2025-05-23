# 常用数据结构

## Reference

- https://leetcode.cn/discuss/post/mOr1u6/

## 前缀和

## 差分


## 常用枚举技巧

### 枚举右，寻找左

对于 双变量问题，例如两数之和 ai+aj=t，可以枚举右边的 aj，转换成 单变量问题，也就是在 aj 左边查找是否有 ai=t−aj，这可以用哈希表维护。
这个技巧叫做 枚举右，寻找左。

1. 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。你可以按任意顺序返回答案。[LC1两数之和](https://leetcode.cn/problems/two-sum/description/)

2. 给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。子数组 是数组的一段连续部分。[LC930](https://leetcode.cn/problems/binary-subarrays-with-sum/description/)



## 栈

### 基础

1. 给你一个数组 target 和一个整数 n。每次迭代，需要从  list = { 1 , 2 , 3 ..., n } 中依次读取一个数字。请使用下述操作来构建目标数组 target ："Push"：从 list 中读取一个新元素， 并将其推入数组中。"Pop"：删除数组中的最后一个元素。如果目标数组构建完成，就停止读取更多元素。题目数据保证目标数组严格递增，并且只包含 1 到 n 之间的数字。请返回构建目标数组所用的操作序列。如果存在多个可行方案，返回任一即可。[LC1441用栈操作构建数组](https://leetcode.cn/problems/build-an-array-with-stack-operations/description/)

    - 初始化空栈
    - 遍历list，list[i]先入栈，如果list[i]不在target，则出栈，
    - 入-更新-出
    - 特判：len(target)==1，没问题



## 队列

## 堆

### 第 K 小/大

> 如果数量关系满足 (i,j)对应< (i,j+1)对应or (i,j+1)对应< (i,j)对应，方法：result数组长度小于k时，(i,j)出堆并存入result，如果(i+1,j)有效且没有访问过，入堆；如果(i,j+1)有效且没有访问过，入堆，当result数组长度大于k，则退出循环，result的末尾就是第k小

1. 给定两个以 非递减顺序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。[LC373](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/description/)

3. 给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。你必须找到一个内存复杂度优于 O(n2) 的解决方案。

    - 可以直到 m[i][j]<m[i+1][j] or m[i][j+1] < m[i+1][j+1]
    - 找到一个 堆 heap = [m[0][0]]
    - m[i][j] 出堆，那么下一个最小值从 (i+1,j)或者(i,j+1)取，再下一个从(i+1,j+1)，注意(i+1,j+1)可以从(i+1,j)推来也可以从(i,j+1)中推来，因此要注意判断是否重复
    

## 字典树

## 并查集

## 树状数组和线段树