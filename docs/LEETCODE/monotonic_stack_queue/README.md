# 单调栈与单调队列


## Reference

- https://leetcode.cn/discuss/post/9oZFK9/
- https://leetcode.cn/discuss/post/3583665/fen-xiang-gun-ti-dan-chang-yong-shu-ju-j-bvmv/


## 单调栈

> 下一个更大/小的数

1. 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。 [LC739](https://leetcode.cn/problems/daily-temperatures/description/)


2. 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。[LC42](https://leetcode.cn/problems/trapping-rain-water/description/)

3. nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。 [LC496](https://leetcode.cn/problems/next-greater-element-i/description/)

4. 给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。[LC503](https://leetcode.cn/problems/next-greater-element-ii/description/)

5. 给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，其中 j 是满足 j > i 且 prices[j] <= prices[i] 的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。[LC1475](https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/description/)


6. 设计一个算法收集某些股票的每日报价，并返回该股票当日价格的 跨度 。当日股票价格的 跨度 被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。例如，如果未来 7 天股票的价格是 [100,80,60,70,60,75,85]，那么股票跨度将是 [1,1,1,2,1,4,6] 。[LC901](https://leetcode.cn/problems/online-stock-span/description/)


1019. 链表中的下一个更大节点 https://leetcode.cn/problems/next-greater-node-in-linked-list/
1944. 队列中可以看到的人数 https://leetcode.cn/problems/number-of-visible-people-in-a-queue/
84. 柱状图中最大的矩形 https://leetcode.cn/problems/largest-rectangle-in-histogram/
1793. 好子数组的最大分数 https://leetcode.cn/problems/maximum-score-of-a-good-subarray/
85. 最大矩形 https://leetcode.cn/problems/maximal-rectangle/


## 单调队列

