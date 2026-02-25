# 二分算法

## Reference

- https://leetcode.cn/discuss/post/3579164/ti-dan-er-fen-suan-fa-er-fen-da-an-zui-x-3rqn/

## 二分查找


- 问题：返回有序数组中第一个$\geq 8$的数的位置，如果所有数都$<8$，返回数组长度.

- 闭区间：L对应数组第一个元素，R对应数组最后一个元素 （红蓝染色法）
    - 取`M=(L+R)//2`
    - 如果`M<8`，那么L到M闭区间数组的部分可以舍去，L跳到M+1，和R组成新的待确认闭区间数组
    - 如果`M>=8`，那么M到R区间数组的部分可以舍去，R跳到M-1，和L组成新的待确认区间
    - 由L和R一直组成闭区间数组可知：L左边的数一定小于8，R右边的数一定大于等于8，所以当L在R的右边的一个位置时，L对应位置就是第一个大于等于8的数.

```bash
5 7 7 7 8 10
L   M      R

5 7 7 7 8 10
      L M  R

5 7 7 7 8 10
      LR 

5 7 7 7 8 10
      R L 
```

- 左闭右开区间：L对应数组第一个元素，R对应数组长度
    - 取`M=(L+R)//2`
    - 如果`M<8`，那么L到M闭区间数组的部分可以舍去，L跳到M+1，和R组成新的左闭右开待确认数组
    - 如果`M>=8`，那么M到R左闭右开区间数组的部分可以舍去，R跳到M，和L组成新的左闭右开待确认区间
    - 由L和R一直组成左闭右开区间数组可知：L左边的数一定小于8，R对应位置及其右边的数一定大于等于8，所以当L=R，L或R对应位置就是第一个大于等于8的数.

```bash
5 7 7 7 8 10
L     M      R

5 7 7 7 8 10
      L M    R

5 7 7 7 8 10
      L R          
```


- 左开右开区间：L对应-1，R对应数组长度
    - 取`M=(L+R)//2`
    - 如果`M<8`，那么L到M左开右闭区间数组的部分可以舍去，L跳到M，和R组成新的左开右开待确认数组
    - 如果`M>=8`，那么M到R左闭右开区间数组的部分可以舍去，R跳到M，和L组成新的左开右开待确认区间
    - 由L和R一直组成左开右开区间数组可知：L对应位置及其左边的数一定小于8，R对应位置及其右边的数一定大于等于8，所以当L在R的左边一个位置，R对应位置就是第一个大于等于8的数.

```bash
  5 7 7 7 8 10
L     M        R

5 7 7 7 8 10
    L   M    R

5 7 7 7 8 10
    L   R        

5 7 7 7 8 10
      L R   

```

```python
def lower_bound(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1  # 闭区间 [left, right]
    while left <= right:  # 区间不为空
        # left + (right - left) // 2
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # [mid+1, right]
        else:
            right = mid - 1  # [left, mid-1]
    return left

def lower_bound2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)  # 左闭右开区间 [left, right)
    while left < right:  # 区间不为空
        # left + (right - left) // 2
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # [mid+1, right)
        else:
            right = mid  # [left, mid)
    return left  # right

def lower_bound3(nums: List[int], target: int) -> int:
    left = -1
    right = len(nums)  # 开区间 (left, right)
    while left + 1 < right:  # 区间不为空
        # left + (right - left) // 2
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid  # (mid, right)
        else:
            right = mid  # (left, mid)
    return right
```

**相比其他二分写法，开区间写法不需要思考加一减一等细节，推荐使用开区间写二分.**



> 有序数组查找

1. 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。如果数组中不存在目标值 target，返回 [-1, -1]。你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。[LC34](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/)

2. 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。请必须使用时间复杂度为 O(log n) 的算法。[LC35](https://leetcode.cn/problems/search-insert-position/description/)

3. 给你一个字符数组 letters，该数组按非递减顺序排序，以及一个字符 target。letters 里至少有两个不同的字符。返回 letters 中大于 target 的最小的字符。如果不存在这样的字符，则返回 letters 的第一个字符。[LC744](https://leetcode.cn/problems/find-smallest-letter-greater-than-target/description/)


4. 给你一个按 非递减顺序 排列的数组 nums ，返回正整数数目和负整数数目中的最大值。换句话讲，如果 nums 中正整数的数目是 pos ，而负整数的数目是 neg ，返回 pos 和 neg二者中的最大值。注意：0 既不是正整数也不是负整数。[LC2529](https://leetcode.cn/problems/maximum-count-of-positive-integer-and-negative-integer/description/)

5. 给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。“距离值” 定义为符合此距离要求的元素数目：对于元素 arr1[i] ，不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。[LC1385](https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/description/)

6. 给你一个长度为 n 的整数数组 nums ，和一个长度为 m 的整数数组 queries 。返回一个长度为 m 的数组 answer ，其中 answer[i] 是 nums 中 元素之和小于等于 queries[i] 的 子序列 的 最大 长度  。子序列 是由一个数组删除某些元素（也可以不删除）但不改变剩余元素顺序得到的一个数组。[LC2389](https://leetcode.cn/problems/longest-subsequence-with-limited-sum/description/)

## 二分答案

### 求最小

> “求最小” 和二分查找求 “排序数组中某元素的第一个位置” 是类似的，按照红蓝染色法，左边是不满足要求的（红色），右边则是满足要求的（蓝色）。

> 求最小：check(mid) == true 时更新 right = mid，反之更新 left = mid，最后返回 right。

1. 给你一个整数数组 nums 和一个正整数 threshold  ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。请你找出能够使上述结果小于等于阈值 threshold 的除数中 最小 的那个。每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。题目保证一定有解。[LC1283](https://leetcode.cn/problems/find-the-smallest-divisor-given-a-threshold/description/)

2. 给你一个数组 time ，其中 time[i] 表示第 i 辆公交车完成 一趟旅途 所需要花费的时间。每辆公交车可以 连续 完成多趟旅途，也就是说，一辆公交车当前旅途完成后，可以 立马开始 下一趟旅途。每辆公交车 独立 运行，也就是说可以同时有多辆公交车在运行且互不影响。给你一个整数 totalTrips ，表示所有公交车 总共 需要完成的旅途数目。请你返回完成 至少 totalTrips 趟旅途需要花费的 最少 时间。[LC2187](https://leetcode.cn/problems/minimum-time-to-complete-trips/description/)

3. 给你一个整数数组 bloomDay，以及两个整数 m 和 k 。现需要制作 m 束花。制作花束时，需要使用花园中 相邻的 k 朵花 。花园中有 n 朵花，第 i 朵花会在 bloomDay[i] 时盛开，恰好 可以用于 一束 花中。请你返回从花园中摘 m 束花需要等待的最少的天数。如果不能摘到 m 束花则返回 -1 。[LC1482](https://leetcode.cn/problems/minimum-number-of-days-to-make-m-bouquets/description/)


### 求最大

> “求最大” 的题目则相反，左边是满足要求的（蓝色），右边是不满足要求的（红色）。这会导致二分写法和上面的 “求最小” 有一些区别。
> 求最大：check(mid) == true 时更新 left = mid，反之更新 right = mid，最后返回 left。
