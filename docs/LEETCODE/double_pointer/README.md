# 双指针

## Reference

- https://leetcode.cn/discuss/post/3578981/ti-dan-hua-dong-chuang-kou-ding-chang-bu-rzz7/

## 单序列双指针

### 相向双指针

> 关键词：反转，排序，两数关系，三数关系

两个指针 `left=0, right=n−1`，从数组的两端开始，向中间移动，这叫**相向双指针**.

1. 编写一个函数，其作用是将输入的字符串反转过来. 输入字符串以字符数组 s 的形式给出. 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题. [LC344反转字符串](https://leetcode.cn/problems/reverse-string/description/) [x]

    - 首尾两个指针 i=0,j=len(s)-1，闭区间
    - s的长度为偶数时，i，j循环交换，直到i>j
    - s的长度为奇数时，i,j循环交换，直到i=j
    - 整合，循环终止于i>=j

2. 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样. 则可以认为该短语是一个 回文串 . 字母和数字都属于字母数字字符. 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false . [LC125验证回文串](https://leetcode.cn/problems/valid-palindrome/description/) [x]

    - 首尾两个指针 i=0,j=len(s)-1，闭区间
    - s的长度为偶数时，i，j循环比较，直到i>j
    - s的长度为奇数时，i,j循环比较，直到i=j
    - 整合，循环终止于i>=j 

1. 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。[LC88](合并两个有序数组)(https://leetcode.cn/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)

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



3. 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序. [LC977有序数组的平方](https://leetcode.cn/problems/squares-of-a-sorted-array/
description/)

    


4. 给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数. 返回的结果必须要是按升序排好的. 整数 a 比整数 b 更接近 x 需要满足：|a - x| < |b - x| 或者 |a - x| == |b - x| 且 a < b. [LC658](https://leetcode.cn/problems/find-k-closest-elements/description/)

5. 给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数. 如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length . 以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2. 你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素. 你所设计的解决方案必须只使用常量级的额外空间. [LC167](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/description/)

6. 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c . [LC633](https://leetcode.cn/problems/sum-of-square-numbers/description/)

7. 给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和两个整数 lower 和 upper ，返回 公平数对的数目 . 如果 (i, j) 数对满足以下情况，则认为它是一个 公平数对 ：0 <= i < j < n，且 lower <= nums[i] + nums[j] <= upper. [LC2563](https://leetcode.cn/problems/count-the-number-of-fair-pairs/description/)

8. 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 . 请你返回所有和为 0 且不重复的三元组. 注意：答案中不可以包含重复的三元组. [LC15](https://leetcode.cn/problems/3sum/description/)

9. 给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数. [LC611](https://leetcode.cn/problems/valid-triangle-number/description/)

10. 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target . 请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：0 <= a, b, c, d < n, a、b、c 和 d 互不相同, nums[a] + nums[b] + nums[c] + nums[d] == target. 你可以按 任意顺序 返回答案 . [LC18](https://leetcode.cn/problems/4sum/description/)

11. 给你两个整数数组 nums1 和 nums2 ，请你返回根据以下规则形成的三元组的数目（类型 1 和类型 2 ）：类型 1：三元组 (i, j, k) ，如果 nums1[i]2 == nums2[j] * nums2[k] 其中 0 <= i < nums1.length 且 0 <= j < k < nums2.length. 类型 2：三元组 (i, j, k) ，如果 nums2[i]2 == nums1[j] * nums1[k] 其中 0 <= i < nums2.length 且 0 <= j < k < nums1.length. [LC1577](https://leetcode.cn/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/description/)

12. 给定一个长度为 n 的整数数组 height . 有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) . 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水. 返回容器可以储存的最大水量. 说明：你不能倾斜容器. [LC11](https://leetcode.cn/problems/container-with-most-water/description/)

13. 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水. [LC42](https://leetcode.cn/problems/trapping-rain-water/description/)

14. 给你一个整数数组 nums 和一个整数 target . 请你统计并返回 nums 中能满足其最小元素与最大元素的 和 小于或等于 target 的 非空 子序列的数目. [LC1498](https://leetcode.cn/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/)

### 同向双指针

> 关键词：子数组

两个指针的移动方向相同（都向右，或者都向左）。之前讲的滑动窗口就是同向双指针. 

1. 给你一个整数数组 arr ，请你删除一个子数组（可以为空），使得 arr 中剩下的元素是 非递减 的。一个子数组指的是原数组中连续的一个子序列。
请你返回满足题目要求的最短子数组的长度。[LC1574](https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/)

2. 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。请你找出符合题意的 最短 子数组，并输出它的长度. [LC581](https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/description/)


### 背向双指针

两个指针从数组中的同一个位置出发，一个向左，另一个向右，背向移动。

### 原地修改

1. 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。[LC27](https://leetcode.cn/problems/remove-element/description/)

2. 给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。[LC26](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/)

3. 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次. [LC80](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/description/)

4. 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。[LC283](https://leetcode.cn/problems/move-zeroes/description/)

5. 给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。[LC905](https://leetcode.cn/problems/sort-array-by-parity/description/)


## 双序列双指针

### 双指针

> 两个序列，一个序列一个指针

1. 给你一个下标从 0 开始的字符串 s ，以及一个下标从 0 开始的整数数组 spaces 。数组 spaces 描述原字符串中需要添加空格的下标。每个空格都应该插入到给定索引处的字符值 之前 。例如，s = "EnjoyYourCoffee" 且 spaces = [5, 9] ，那么我们需要在 'Y' 和 'C' 之前添加空格，这两个字符分别位于下标 5 和下标 9 。因此，最终得到 "Enjoy Your Coffee" 。请你添加空格，并返回修改后的字符串。[LC2109](https://leetcode.cn/problems/adding-spaces-to-a-string/description/)

2. 给你两个整数数组 nums1 和 nums2 ，它们已经按非降序排序，请你返回两个数组的 最小公共整数 。如果两个数组 nums1 和 nums2 没有公共整数，请你返回 -1 。如果一个整数在两个数组中都 至少出现一次 ，那么这个整数是数组 nums1 和 nums2 公共 的。[LC2540](https://leetcode.cn/problems/minimum-common-value/description/)

3. 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。[LC88](https://leetcode.cn/problems/merge-sorted-array/description/)

4. 给你两个 非递增 的整数数组 nums1​​​​​​ 和 nums2​​​​​​ ，数组下标均 从 0 开始 计数。下标对 (i, j) 中 0 <= i < nums1.length 且 0 <= j < nums2.length 。如果该下标对同时满足 i <= j 且 nums1[i] <= nums2[j] ，则称之为 有效 下标对，该下标对的 距离 为 j - i​​ 。​​返回所有 有效 下标对 (i, j) 中的 最大距离 。如果不存在有效下标对，返回 0 。[LC1855](https://leetcode.cn/problems/maximum-distance-between-a-pair-of-values/description/)

5. 在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个 "LX" 替换一个 "XL"，或者用一个 "XR" 替换一个 "RX"。现给定起始字符串 start 和结束字符串 result，请编写代码，当且仅当存在一系列移动操作使得 start 可以转换成 result 时， 返回 True。[LC777](https://leetcode.cn/problems/swap-adjacent-in-lr-string/description/)

6. 给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。返回这 两个区间列表的交集 。[LC986](https://leetcode.cn/problems/interval-list-intersections/description/)

### 判断子序列

> 判断a是否为b的子序列

1. 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。子序列是一个可以由其他字符串删除部分（或不删除）字符但不改变剩下字符顺序得到的字符串。[LC392](https://leetcode.cn/problems/is-subsequence/description/)

2. 给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。[LC524](https://leetcode.cn/problems/longest-word-in-dictionary-through-deleting/description/)

3. 给你两个仅由小写英文字母组成的字符串 s 和 t 。现在需要通过向 s 末尾追加字符的方式使 t 变成 s 的一个 子序列 ，返回需要追加的最少字符数。[LC2486](https://leetcode.cn/problems/append-characters-to-string-to-make-subsequence/description/)

## 三指针

1. 给你一个下标从 0 开始、严格递增 的整数数组 nums 和一个正整数 diff 。如果满足下述全部条件，则三元组 (i, j, k) 就是一个 等差三元组 ：i < j < k ，nums[j] - nums[i] == diff 且 nums[k] - nums[j] == diff. 返回不同 等差三元组 的数目。[LC2367](https://leetcode.cn/problems/number-of-arithmetic-triplets/description/)

2. 给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right] 内的子数组，并返回满足条件的子数组的个数。[LC795](https://leetcode.cn/problems/number-of-subarrays-with-bounded-maximum/description/)

## 分组循环

> 有约束条件的子数组

> 适用场景：按照题目要求，数组会被分割成若干组，每一组的判断/处理逻辑是相同的。

> 核心思想：
> - 外层循环负责遍历组之前的准备工作（记录开始位置），和遍历组之后的统计工作（更新答案最大值）。
> - 内层循环负责遍历组，找出这一组最远在哪结束。
这个写法的好处是，各个逻辑块分工明确，也不需要特判最后一组（易错点）。



1. 给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。请你返回字符串 s 的 能量。[LC1446](https://leetcode.cn/problems/consecutive-characters/)

2. 给你一个二进制字符串 s 。如果字符串中由 1 组成的 最长 连续子字符串 严格长于 由 0 组成的 最长 连续子字符串，返回 true ；否则，返回 false 。[LC1869](https://leetcode.cn/problems/longer-contiguous-segments-of-ones-than-zeros/description/)

3. 字母序连续字符串 是由字母表中连续字母组成的字符串。换句话说，字符串 "abcdefghijklmnopqrstuvwxyz" 的任意子字符串都是 字母序连续字符串 。例如，"abc" 是一个字母序连续字符串，而 "acb" 和 "za" 不是。
给你一个仅由小写英文字母组成的字符串 s ，返回其 最长 的 字母序连续子字符串 的长度。[LC2414](https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/description/)

4. 给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。[LC674](https://leetcode.cn/problems/longest-continuous-increasing-subsequence/description/)

5. 给定一个  无重复元素 的 有序 整数数组 nums 。返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。列表中的每个区间范围 [a,b] 应该按如下格式输出："a->b" ，如果 a != b；"a" ，如果 a == b. [LC228](https://leetcode.cn/problems/summary-ranges/description/)

6. 给你一个字符串 s ，返回 s 中 同质子字符串 的数目。同质字符串 的定义为：如果一个字符串中的所有字符都相同，那么该字符串就是同质字符串. [LC1759](https://leetcode.cn/problems/count-number-of-homogenous-substrings/description/)

7. 给你一个整数数组 prices ，表示一支股票的历史每日股价，其中 prices[i] 是这支股票第 i 天的价格。一个 平滑下降的阶段 定义为：对于 连续一天或者多天 ，每日股价都比 前一日股价恰好少 1 ，这个阶段第一天的股价没有限制。请你返回 平滑下降阶段 的数目。[LC2110](https://leetcode.cn/problems/number-of-smooth-descent-periods-of-a-stock/description/)

8. 给你一个下标从 0 开始的整数数组 nums 。如果 nums 中长度为 m 的子数组 s 满足以下条件，我们称它是一个 交替子数组 ：
    - m 大于 1 。
    - s1 = s0 + 1 。
    - 下标从 0 开始的子数组 s 与数组 [s0, s1, s0, s1,...,s(m-1) % 2] 一样。也就是说，s1 - s0 = 1 ，s2 - s1 = -1 ，s3 - s2 = 1 ，s4 - s3 = -1 ，以此类推，直到 s[m - 1] - s[m - 2] = (-1)m 。
请你返回 nums 中所有 交替 子数组中，最长的长度，如果不存在交替子数组，请你返回 -1 。[LC2765](https://leetcode.cn/problems/longest-alternating-subarray/description/)