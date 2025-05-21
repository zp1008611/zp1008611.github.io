# LEETCODE刷题模板

## 心得

- 做题先手打一下思路，然后再写代码，注意分点，从边界点开始到常规点
- 题目使用数组和链表这两个数据结构时，最好对空数组进行特判. 
- 判断两个区间[a,b],[c,d]是否有交集，`(a<d and c<d)`为True，则有交集
- python下判断两个集合是否有交集，`set([1,2,3]) & set([2,3,4])`为True，则有交集
- 对于双变量问题，判断那两个值满足某种关系，可以使用数组枚举右，哈希寻找左的方法
- dp中爬楼梯问题，要区别楼梯和平台，有n个楼梯就有n+1个平台（最低的平台的是地平面，最高的平台是第n个楼梯对应平行地平面的平台）
- 网格dp，先对网格大小m，n进行0特判，再对dp数组中的边界特判，最后再进行常规操作
- 题目找满足某种要求且长度为k的子数组/字串，常用定长滑窗，初始化时滑窗长度为k-1，按入-更新-出进行操作；如果要求滑窗内的元素不重复，那么还需要维护一个哈希表，在入元素对哈希表进行更新，并遍历哈希，如果哈希表有重复元素，滑窗左边出元素，哈希表更新，直至滑窗元素不重复
- DFS：起点入栈->循环：（出栈->没访问过的出栈点的邻居逆序入栈）
- 对于网格DFS，要注意网格图的x，y坐标表示，假设m=len(grid),n=len(grid[0])，那么x的范围为0-n，y的范围为0-m

## 刷题优先级

刷题顺序：dp->dfs&bfs->二叉树->树形dp->滑窗->枚举技巧->双指针->二分

dp,dfs,二叉树我分为一类题（递归），枚举，双指针，滑窗，二分我分为另一类题（指针）

一类题刷累了，可以刷另一类

## 数论

1. 判断一个数是否为素数

    ```python
    import math
    def is_prime_optimized(num):
        if num < 2:
            return False
        limit = int(math.sqrt(num)) + 1
        for i in range(2, limit):
            if num % i == 0:
                return False
        return True
    ```

2. 找出`0`到`n`以内的所有素数

    ```python
    import math
    def find_primes_optimized(n):
        primes = []
        for num in range(2, n + 1):
            is_prime = True
            limit = int(math.sqrt(num)) + 1
            for i in range(2, limit):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes
    ```
3. 找出一个数的所有质因子

    ```python
    def prime_factors(n):
        factors = []
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n = n // divisor
            divisor = divisor + 1
        return factors
    ```

4. 找出一个数的所有因子

    ```python
    import math
    def find_factors_optimized(num):
        factors = []
        limit = int(math.sqrt(num))
        for i in range(1, limit + 1):
            if num % i == 0:
                factors.append(i)
                if i != num // i:
                    factors.append(num // i)
        factors.sort()
        return factors
    ```

5. 求最大公因数和最小公倍数

    ```python
    import math

    def gcd(a,b):
        return math.gcd(a,b)

    def lcm(a, b):
        return a * b // math.gcd(a, b)

    ```

## 离散化

离散化是当仅关注数据大小关系时，用排名替代原数据的预处理手段，属于哈希的一种，能将数据映射为正整数，适用于原数据值过大或含负数、小数等情形. 以序列$A = [10, 23, 35, 3, -40, 3]$为例，先复制序列得$C$，对$C$排序、去重，得到不重复元素数组$C = [-40, 3, 10, 23, 35]$ ；再通过二分查找确定$A$中元素在$C$中的排名，最终离散化结果为$L = [3, 4, 5, 2, 1, 2]$ . 排序和$n$次二分查找时间复杂度均为$O(n\log n)$，故离散化整体时间复杂度为$O(n\log n)$ ，也可依需求从大到小排序. 

```python
def discretize(arr):
    # 复制并去重排序
    sorted_unique_arr = sorted(set(arr))
    # 构建元素到排名的映射字典
    rank_dict = {num: rank + 1 for rank, num in enumerate(sorted_unique_arr)}
    # 得到离散化后的数组
    result = [rank_dict[num] for num in arr]
    return result

# 示例使用
arr = [10, 23, 35, 3, -40, 3]
print(discretize(arr))
``` 

离散化常常和前缀和与dp结合使用.

## 前缀和

前缀和技巧主要应用于原始数组不会被修改，却需要频繁查询某个区间累加和的场景.

```python
class PrefixSum:
    # 前缀和数组
    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        # 计算 nums 的累加和
        for i in range(1, len(self.prefix)):
            self.prefix[i] = self.prefix[i - 1] + nums[i - 1]
    
    # 查询闭区间 [i, j] 的累加和
    def query(self, i: int, j: int) -> int:
        return self.prefix[j + 1] - self.prefix[i]
```

## 差分

频繁对原始数组的某个区间元素进行增减得到新的数组.

```python
class Difference:
    def __init__(self, nums):
        assert len(nums) > 0
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    def increment(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val

    def result(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
        return res

```

## 快速幂

给定两个整数a和b，现在想让你求出a的b次方对1e9+7取模后的值
- 快速幂算法是一种用于高效计算 $a^b$ 的算法. 其核心思想是利用指数的二进制表示，通过不断平方底数并根据指数的二进制位决定是否累乘，从而将时间复杂度从朴素的 $O(b)$ 降低到 $O(\log b)$ . 
- 对于 $a^b$ ，将 $b$ 转换为二进制形式，例如 $b = \sum_{i = 0}^{n}k_{i}2^{i}$ ，其中 $k_{i}$ 为 $0$ 或 $1$ . 那么 $a^b=a^{\sum_{i = 0}^{n}k_{i}2^{i}}=\prod_{i = 0}^{n}(a^{2^{i}})^{k_{i}}$ . 
- 在计算过程中，我们不断计算 $a^{2^i}$ （通过不断平方 $a$ 得到），并且当 $k_{i}=1$ 时，将其累乘到结果中. 
- 取模运算遵循 $(a\times b)\%m = ((a\%m)\times(b\%m))\%m$ 的性质，所以在快速幂计算过程中可以随时进行取模操作，避免数值过大. 

```python
MOD = 10 ** 9 + 7
def fast_power(a, b):
    result = 1
    a = a % MOD
    while b > 0:
        if b & 1:
            result = (result * a) % MOD
        a = (a * a) % MOD
        b >>= 1
    return result


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(fast_power(a, b))
```


## 位运算

1. 二进制数转整数

    ```python
    # 定义二进制字符串
    binary_str = '1010'
    # 使用 int() 函数将二进制字符串转换为整数
    decimal_num = int(binary_str, 2)
    print(f"二进制字符串 {binary_str} 转换为整数是: {decimal_num}")
    ```

2. 整数转二进制数

    ```python
    # 定义一个整数
    decimal_num = 10
    # 使用 bin() 函数将整数转换为二进制字符串，并去除 '0b' 前缀
    binary_str = bin(decimal_num)[2:]
    print(f"整数 {decimal_num} 转换为无 '0b' 前缀的二进制字符串是: {binary_str}")
    ```

3. 整数转自定义位数的二进制数  

    ```python
    # 定义一个整数
    decimal_num = 10
    # 定义所需的二进制位数
    bit_length = 8
    # 使用 bin() 函数将整数转换为二进制字符串，去除 '0b' 前缀，并进行零填充
    binary_str = bin(decimal_num)[2:].zfill(bit_length)
    print(f"整数 {decimal_num} 转换为 {bit_length} 位的二进制字符串是: {binary_str}")
    ```

4. 位运算
    - 左移操作会把一个数的二进制表示向左移动指定的位数，右边空出的位用 0 填充. 每向左移动一位，相当于该数乘以 2；向左移动 n 位，就相当于该数乘以 2^n. 
    - 右移操作会把一个数的二进制表示向右移动指定的位数. 根据移动对象是有符号数还是无符号数，右移分为逻辑右移和算术右移. 不过在 Python 里，整数类型没有明确的有符号和无符号之分，Python 的右移操作更类似于算术右移，对于正数，左边空出的位用 0 填充；对于负数，左边空出的位用 1 填充. 每向右移动一位，相当于该数除以 2 并向下取整. 
    - 按位与运算会对两个整数的二进制表示的每一位进行逻辑与操作. 只有当对应位都为 1 时，结果的该位才为 1，否则为 0. 
    - 按位或运算符（|）用于对两个二进制操作数的对应位执行逻辑或运算，只要两个对应位中有一个为 1，结果位就为 1，只有当两个对应位都为 0 时，结果位才为 0. 
    - 异或运算（`^`）是一种二进制逻辑运算，当两个操作数的对应位不同时，结果为1；相同时，结果为0

5. 提取二进制数第`n`位的数

    ```python
    num = 25  # 二进制表示为 11001
    n = 1
    bit = (num >> n) & 1
    print(f"第 {n} 位是: {bit}")
    ```

6. 求两个集合的交集

    ```python
    # 假设集合元素用整数表示，且每个元素对应二进制中的一位
    # 定义两个集合
    set1 = {1, 2, 4, 8}
    set2 = {2, 4, 16}

    # 将集合转换为对应的二进制数
    def set_to_binary(s):
        binary = 0
        for element in s:
            binary |= 1 << element
        return binary

    # 将二进制数转换回集合
    def binary_to_set(binary):
        result = set()
        index = 0
        while binary:
            if binary & 1:
                result.add(index)
            binary >>= 1
            index += 1
        return result

    # 将集合转换为二进制数
    binary1 = set_to_binary(set1)
    binary2 = set_to_binary(set2)

    # 通过按位与操作得到交集的二进制表示
    intersection_binary = binary1 & binary2

    # 将二进制表示转换回集合
    intersection = binary_to_set(intersection_binary)

    print("集合1:", set1)
    print("集合2:", set2)
    print("交集:", intersection)
    ```

7. 判断元素是否在集合中. 

    ```python
    def is_element_in_set(element, set_bits):
        return (set_bits & (1 << element)) != 0

    # 假设集合对应的二进制数为 0b1011，表示集合包含元素 0、1、3
    set_bits = 0b1011
    element_to_check = 2
    if is_element_in_set(element_to_check, set_bits):
        print(f"元素 {element_to_check} 在集合中")
    else:
        print(f"元素 {element_to_check} 不在集合中")
    ```

8. 枚举集合所有子集

    ```python
    def enumerate_subsets(set_list):
        n = len(set_list)
        all_subsets = []
        # 遍历从 0 到 2^n - 1 的所有整数
        for i in range(1 << n):
            subset = []
            for j in range(n):
                # 检查第 j 位是否为 1
                if i & (1 << j):
                    subset.append(set_list[j])
            all_subsets.append(subset)
        return all_subsets


    # 示例集合
    set_list = [1, 2, 3]
    subsets = enumerate_subsets(set_list)
    for subset in subsets:
        print(subset)
    ```

9. 枚举所有非空子集

    ```python
    def enumerate_non_empty_subsets(set_list):
        n = len(set_list)
        non_empty_subsets = []
        # 从 1 开始遍历到 2^n - 1
        for i in range(1, 1 << n):
            subset = []
            for j in range(n):
                # 检查第 j 位是否为 1
                if i & (1 << j):
                    subset.append(set_list[j])
            non_empty_subsets.append(subset)
        return non_empty_subsets


    # 示例集合
    set_list = [1, 2, 3]
    subsets = enumerate_non_empty_subsets(set_list)
    for subset in subsets:
    print(subset)
    ```

## 回溯

1. 从 `n` 个元素中选取 `k` 个元素的所有组合. 

    ```python
    def combine(n, k):
        result = []

        def backtrack(start, path):
            # 当路径中的元素个数达到 k 时，说明找到了一个有效的组合
            if len(path) == k:
                result.append(path[:])
                return
            # 从 start 开始遍历到 n，尝试添加元素到路径中
            for i in range(start, n + 1):
                path.append(i)
                # 递归调用，继续寻找下一个元素
                backtrack(i + 1, path)
                # 回溯操作，撤销上一步的选择
                path.pop()

        backtrack(1, [])
        return result

    # 示例
    n = 4
    k = 2
    print(combine(n, k))
    ```

2. 生成 `n` 个元素的所有排列. 

    ```python
    def permute(nums):
        result = []
        def backtrack(path, used):
            # 当路径的长度等于数组的长度时，说明找到了一个完整的排列
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                # 如果该元素已经在路径中，跳过
                if used[i]:
                    continue
                # 选择当前元素
                used[i] = True
                path.append(nums[i])
                # 递归探索
                backtrack(path, used)
                # 回溯，撤销选择
                used[i] = False
                path.pop()

        # 初始化使用标记数组
        used = [False] * len(nums)
        backtrack([], used)
        return result

    # 示例
    nums = [1, 2, 3]
    print(permute(nums))
    ```

3. 求和为 target 且元素个数为 k 的组合

    ```python
    def combination_sum_k(nums, k, target):
        def backtrack(start, path, current_sum, current_count):
            # 如果当前组合的元素个数达到 k 且和等于 target，则将该组合添加到结果中
            if current_count == k and current_sum == target:
                result.append(path[:])
                return
            # 如果当前组合的元素个数超过 k 或者和超过 target，则停止搜索
            if current_count > k or current_sum > target:
                return
            # 从 start 开始遍历数组
            for i in range(start, len(nums)):
                # 选择当前元素
                path.append(nums[i])
                # 递归搜索下一个元素
                backtrack(i + 1, path, current_sum + nums[i], current_count + 1)
                # 回溯，撤销选择
                path.pop()

        result = []
        backtrack(0, [], 0, 0)
        return result


    # 示例
    nums = [1, 2, 3, 4, 5]
    k = 3
    target = 9
    print(combination_sum_k(nums, k, target))
    ```

## 各种排序方法

1. 交换排序（通过元素交换实现排序）
    - **冒泡排序**
        - 基本思想：相邻元素两两比较，逆序时交换，每轮将最大元素 “冒泡” 到末尾。
        - 步骤：从左到右遍历数组，比较相邻元素，若前＞后则交换；重复上述过程，直到某轮无交换（数组已有序）。
        - 核心代码：

        ```python
        def bubble_sort(arr):
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr
        ```

    - **快速排序**
        - 基本思想：分治策略，选择基准值（Pivot），将数组分为＜基准和＞基准两部分，递归排序子数组。
        - 步骤：选基准（通常选第一个、最后一个或中间元素）；分区：比基准小的放左边，大的放右边；递归排序左右子数组。
        - 核心代码：

        ```python
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quick_sort(left) + middle + quick_sort(right)
        ```

2. 插入排序（逐步构建有序序列）
    - **直接插入排序**
        - 基本思想：将未排序元素逐个插入已排序序列的合适位置。
        - 步骤：假设前i个元素已有序，第i + 1个元素从后往前比较，找到位置插入。
        - 核心代码：

        ```python
        def insertion_sort(arr):
            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j = j - 1
                arr[j + 1] = key
            return arr
        ```

    - **希尔排序**
        - 基本思想：插入排序的改进，通过“增量”分组，对每组进行插入排序，逐步缩小增量至1。
        - 步骤：选择增量序列（如n/2, n/4, …, 1），按增量分组，组内插入排序；增量为1时，退化为直接插入排序。
        - 核心代码：

        ```python
        def shell_sort(arr):
            n = len(arr)
            gap = n // 2
            while gap > 0:
                for i in range(gap, n):
                    temp = arr[i]
                    j = i
                    while j >= gap and arr[j - gap] > temp:
                        arr[j] = arr[j - gap]
                        j = j - gap
                    arr[j] = temp
                gap = gap // 2
            return arr

        ```

3. 选择排序（选择最小元素逐步构建有序序列）
    - **直接选择排序**
        - 基本思想：每轮从未排序部分选最小元素，与未排序部分第一个元素交换。
        - 步骤：第i轮在[i, n - 1]找最小元素，与第i个元素交换。
        - 核心代码：

        ```python
        def selection_sort(arr):
            n = len(arr)
            for i in range(n):
                min_idx = i
                for j in range(i + 1, n):
                    if arr[j] < arr[min_idx]:
                        min_idx = j
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
            return arr
        ```

    - **堆排序**
        - 基本思想：利用堆结构（大顶堆或小顶堆），每次取堆顶元素（最大/最小），重构堆直到有序。
        - 步骤：构建大顶堆（父节点≥子节点）；交换堆顶与末尾元素，对前n - 1个元素重构堆，重复直到排序完成。
        - 核心代码：

        ```python
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[l] > arr[largest]:
                largest = l
            if r < n and arr[r] > arr[largest]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)


        def heap_sort(arr):
            n = len(arr)
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)
            return arr

        ```

4. 归并排序（分治 + 合并）
    - **归并排序**
        - 基本思想：分治策略，将数组分成两半，递归排序，再合并两个有序子数组。
        - 步骤：分解：将数组分成左右两半，直到子数组长度为1；合并：将两个有序子数组合并为一个有序数组。
        - 核心代码：

        ```python
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                L = arr[:mid]
                R = arr[mid:]
                merge_sort(L)
                merge_sort(R)
                i = j = k = 0
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i = i + 1
                    else:
                        arr[k] = R[j]
                        j = j + 1
                    k = k + 1
                while i < len(L):
                    arr[k] = L[i]
                    i = i + 1
                    k = k + 1
                while j < len(R):
                    arr[k] = R[j]
                    j = j + 1
                    k = k + 1
            return arr
        ```

5. 线性时间排序（非比较排序，需特定条件）
    - **计数排序**
        - 基本思想：统计每个元素出现次数，按次数重排数组。
        - 步骤：统计每个元素出现次数；计算前缀和确定元素位置；按位置填充结果数组。
        - 核心代码：

        ```python
        def counting_sort(arr):
            max_val = max(arr)
            count = [0] * (max_val + 1)
            for num in arr:
                count[num] = count[num] + 1
            index = 0
            for i in range(len(count)):
                while count[i] > 0:
                    arr[index] = i
                    index = index + 1
                    count[i] = count[i] - 1
            return arr
        ```

    - **基数排序**
        - 基本思想：按元素每一位（个位、十位、百位…）排序，从低位到高位依次进行。
        - 步骤：对每一位（如十进制的个位、十位），用稳定排序（如计数排序）排序元素；低位排序完成后，高位排序时保留低位顺序。
        - 核心代码：

        ```python
        def counting_sort_for_radix(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10
            for i in range(n):
                index = arr[i] // exp
                count[index % 10] = count[index % 10] + 1
            for i in range(1, 10):
                count[i] = count[i] + count[i - 1]
            i = n - 1
            while i >= 0:
                index = arr[i] // exp
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] = count[index % 10] - 1
                i = i - 1
            i = 0
            for i in range(0, len(arr)):
                arr[i] = output[i]


        def radix_sort(arr):
            max_num = max(arr)
            exp = 1
            while max_num // exp > 0:
                counting_sort_for_radix(arr, exp)
                exp = exp * 10
            return arr

        ``` 


## 栈

1. 每日温度
    - **题目描述**：给定一个整数数组 `temperatures` ，表示每天的温度，返回一个数组 `answer` ，其中 `answer[i]` 是指对于第 `i` 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 `0` 来代替。
    - **解题思路**：使用单调栈来解决。从左到右遍历温度数组，对于每个温度，将其下标和温度作为一个二元组压入栈中。在压入之前，先检查栈顶元素对应的温度是否小于当前温度，如果是，则说明找到了下一个更高的温度，计算两者的下标差并更新结果数组，然后将栈顶元素弹出，继续检查栈顶元素，直到栈为空或者栈顶元素对应的温度大于当前温度。最后，将当前温度的下标和温度压入栈中。
    - **示例代码**

    ```python
    def dailyTemperatures(temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                prev_i, _ = stack.pop()
                answer[prev_i] = i - prev_i
            stack.append((i, temp))
        return answer
    ```

2. 柱状图中最大的矩形
    - **题目描述**：给定 `n` 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 `1` 。求在该柱状图中，能够勾勒出来的矩形的最大面积。
    - **解题思路**：使用单调栈来解决。从左到右遍历柱状图的高度数组，对于每个柱子，将其下标和高度作为一个二元组压入栈中。在压入之前，先检查栈顶元素对应的高度是否大于当前柱子的高度，如果是，则说明找到了一个可以形成矩形的区域，计算该矩形的面积并更新最大面积，然后将栈顶元素弹出，继续检查栈顶元素，直到栈为空或者栈顶元素对应的高度小于当前柱子的高度。最后，将当前柱子的下标和高度压入栈中。遍历完整个数组后，还需要检查栈中剩余的元素，计算它们对应的矩形面积并更新最大面积。
    - **示例代码**

    ```python
    def largestRectangleArea(heights):
        stack = []
        max_area = 0
        n = len(heights)
        for i in range(n):
            while stack and heights[i] < stack[-1][1]:
                index, height = stack.pop()
                width = i - stack[-1][0] - 1 if stack else i
                max_area = max(max_area, width * height)
            stack.append((i, heights[i]))
        while stack:
            index, height = stack.pop()
            width = n - stack[-1][0] - 1 if stack else n
            max_area = max(max_area, width * height)
        return max_area
    ```

## 队列

1. 滑动窗口最大值
    - **题目描述**：给定一个数组 `nums` 和一个整数 `k` ，有一个大小为 `k` 的滑动窗口从数组的最左侧移动到数组的最右侧。你只能看到在滑动窗口内的 `k` 个数字。滑动窗口每次只向右移动一位。返回滑动窗口中的最大值。
    - **解题思路**：使用单调队列来解决。维护一个单调递减的队列，队列中存储数组元素的下标。遍历数组，对于每个元素，先将队列中小于当前元素的下标弹出，然后将当前元素的下标加入队列。在加入下标之前，需要判断队列头部的下标是否已经超出了滑动窗口的范围，如果是，则将其弹出。每次遍历到新元素时，队列头部的下标对应的元素就是当前滑动窗口中的最大值。
    - **示例代码**

    ```python
    from collections import deque

    def maxSlidingWindow(nums, k):
        queue = deque()
        result = []
        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if queue[0] <= i - k:
                queue.popleft()
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result
    ```


## 堆

堆是一种特殊的数据结构，常考的算法题主要围绕堆的基本操作和应用展开，以下是一些常见的堆算法题：

1. 前K个高频元素
    - **题目描述**：给定一个非空的整数数组，返回其中出现频率前 `k` 高的元素。
    - **解题思路**：可以使用哈希表来统计每个元素出现的频率，然后将频率和元素组成一个二元组，放入最小堆中。当堆的大小超过 `k` 时，弹出堆顶元素。最后堆中剩下的元素就是出现频率前 `k` 高的元素。
    - **示例代码**

    ```python
    import heapq
    from collections import Counter

    def topKFrequent(nums, k):
        # 统计每个元素出现的频率
        freq = Counter(nums)
        # 创建一个最小堆
        heap = []
        # 将频率和元素放入堆中
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            # 如果堆的大小超过k，弹出堆顶元素
            if len(heap) > k:
                heapq.heappop(heap)
        # 返回前k个高频元素
        return [heapq.heappop(heap)[1] for _ in range(k)][::-1]
    ```

2. 最小的K个数
    - **题目描述**：输入整数数组 `arr` ，找出其中最小的 `k` 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
    - **解题思路**：可以使用最大堆来解决。先将数组中前 `k` 个元素构建成一个最大堆，然后从第 `k+1` 个元素开始遍历数组，对于每个元素，如果它小于堆顶元素，则将堆顶元素弹出，将该元素插入堆中。最后堆中的元素就是最小的 `k` 个数。
    - **示例代码**

    ```python
    import heapq

    def getLeastNumbers(arr, k):
        if k == 0:
            return []
        # 取数组中前k个元素构建最大堆
        heap = [-x for x in arr[:k]]
        heapq.heapify(heap)
        # 遍历数组中剩余的元素
        for i in range(k, len(arr)):
            # 如果当前元素小于堆顶元素，则将堆顶元素弹出，将当前元素插入堆中
            if arr[i] < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -arr[i])
        # 返回最小的k个数
        return [-x for x in heap]
    ```


## 双端队列

双端队列（Deque）是一种具有队列和栈性质的数据结构，允许在两端进行插入和删除操作。以下是一些双端队列常考的算法题：

1. 回文排列
    - **题目描述**：给定一个字符串，判断该字符串是否可以通过重新排列组合成一个回文串。
    - **解题思路**：可以使用双端队列和哈希表来解决。首先使用哈希表统计每个字符出现的次数，然后将出现偶数次的字符加入双端队列，对于出现奇数次的字符，最多只能有一个。最后，从双端队列的两端取出字符，组成回文串。如果能够组成回文串，则说明原字符串可以通过重新排列组合成一个回文串。
    - **示例代码**

    ```python
    from collections import deque, Counter

    def canPermutePalindrome(s):
        # 统计每个字符出现的次数
        count = Counter(s)
        # 记录出现奇数次的字符个数
        odd_count = 0
        # 创建双端队列
        deq = deque()
        for char, freq in count.items():
            if freq % 2 == 1:
                odd_count += 1
                if odd_count > 1:
                    return False
            # 将出现偶数次的字符加入双端队列
            for _ in range(freq // 2):
                deq.append(char)
        # 从双端队列的两端取出字符，组成回文串
        palindrome = ''
        while deq:
            palindrome += deq.popleft()
        # 如果字符串长度为奇数，将出现奇数次的字符添加到中间
        if len(s) % 2 == 1:
            palindrome += [char for char, freq in count.items() if freq % 2 == 1][0]
        # 从双端队列的后端取出字符，组成回文串的后半部分
        while deq:
            palindrome += deq.pop()
        return True
    ```


## 优先队列


1. 最小会议室数量
    - **题目描述**：给定一系列的会议时间间隔，包括起始和结束时间 `[[s1,e1],[s2,e2],...]`（`si < ei`），请你计算至少需要多少间会议室，才能满足这些会议的需求。
    - **解题思路**：首先将所有会议按照开始时间进行排序。然后使用优先队列（最小堆）来维护会议室的结束时间。遍历排序后的会议列表，对于每个会议，检查优先队列中最早结束的会议时间是否早于当前会议的开始时间。如果是，则可以使用该会议室，将其结束时间更新为当前会议的结束时间；否则，需要分配一个新的会议室，并将当前会议的结束时间加入优先队列。最后，优先队列中元素的个数就是所需的最小会议室数量。
    - **示例代码**

    ```python
    import heapq

    def minMeetingRooms(intervals):
        # 按照会议开始时间对会议进行排序
        intervals.sort(key=lambda x: x[0])
        # 创建优先队列（最小堆），用于存储会议室的结束时间
        heap = []
        for interval in intervals:
            start, end = interval
            if heap and heap[0] <= start:
                # 如果最早结束的会议室在当前会议开始前结束，则可以使用该会议室
                heapq.heapreplace(heap, end)
            else:
                # 否则，需要分配一个新的会议室
                heapq.heappush(heap, end)
        return len(heap)
    ```


## 树的各种遍历方法

树的遍历方法主要有以下几种：

假设我们有一棵二叉树，其结构如下：

```
      1
    /   \
   2     3
  / \   / \
 4   5 6   7
```

用代码创建这棵树：

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
```

1. **先序遍历**：先访问根节点，然后递归遍历左子树，最后递归遍历右子树。
结果：`[1, 2, 4, 5, 3, 6, 7]`

2. **中序遍历**：先递归遍历左子树，然后访问根节点，最后递归遍历右子树。
结果：`[4, 2, 5, 1, 6, 3, 7]`

3. **后序遍历**：先递归遍历左子树，然后递归遍历右子树，最后访问根节点。
结果：`[4, 5, 2, 6, 7, 3, 1]`

4. **层次遍历**：按层次从根节点开始访问，先访问第一层（根节点），然后访问第二层（根节点的子节点），以此类推。
结果：`[[1], [2, 3], [4, 5, 6, 7]]`

下面是实现这些遍历的完整代码：

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# 先序遍历
def preorder_traversal(root):
    result = []
    if root:
        result.append(root.val)
        result.extend(preorder_traversal(root.left))
        result.extend(preorder_traversal(root.right))
    return result

# 中序遍历
def inorder_traversal(root):
    result = []
    if root:
        result.extend(inorder_traversal(root.left))
        result.append(root.val)
        result.extend(inorder_traversal(root.right))
    return result

# 后序遍历
def postorder_traversal(root):
    result = []
    if root:
        result.extend(postorder_traversal(root.left))
        result.extend(postorder_traversal(root.right))
        result.append(root.val)
    return result

# 层次遍历
from collections import deque
def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_result = []
        for _ in range(level_size):
            node = queue.popleft()
            level_result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_result)
    return result

print("先序遍历结果:", preorder_traversal(root))
print("中序遍历结果:", inorder_traversal(root))
print("后序遍历结果:", postorder_traversal(root))
print("层次遍历结果:", level_order_traversal(root))

``` 

## 树状数组

树状数组的单点更新和区间求和的功能：

```python
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        # 树状数组，初始值都为0
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        # 单点更新操作，将第i个元素增加val
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        # 区间求和操作，计算前i个元素的和
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

# 使用示例
bit = BinaryIndexedTree(10)
bit.update(3, 5)  # 将第3个元素增加5
bit.update(5, 3)  # 将第5个元素增加3
print(bit.query(5))  # 输出前5个元素的和，应该为8
```

## 二分搜索
二分搜索（Binary Search），也称为折半搜索，是一种在有序数组中查找特定元素的算法。它的基本思想是：每次将搜索区间缩小一半，通过比较目标元素与区间中间元素的大小，来确定下一步搜索的区间，直到找到目标元素或者确定目标元素不存在。

1. 找到K个最接近的元素
    - **题目描述**：给定一个排序好的数组 `arr`，两个整数 `k` 和 `x`，从数组中找到最接近 `x` 的 `k` 个整数。返回的结果应该按升序排列。如果有多个相同距离的元素，较小的元素优先。
    - **解题思路**：首先使用二分搜索找到 `x` 在数组中的插入位置 `pos`。然后从 `pos` 开始向两边扩展，维护一个大小为 `k` 的窗口，每次比较窗口两端元素与 `x` 的距离，将距离较大的元素移除，直到窗口大小为 `k`。
    - **示例代码**

    ```python
    def findClosestElements(arr, k, x):
        # 使用二分搜索找到x在数组中的插入位置
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        # 从插入位置开始向两边扩展，维护大小为k的窗口
        pos = left
        left, right = pos - k, pos
        while left < 0:
            right += 1
        while right < len(arr) and (x - arr[left]) > (arr[right] - x):
            left += 1
        while left > 0 and (x - arr[left - 1]) <= (arr[right] - x):
            left -= 1
        return arr[left:left + k]
    ```

## BFS和DFS
假设图以邻接表的形式存储，邻接表是一个字典，键是节点，值是该节点的邻居节点列表。

1. 广度优先搜索（BFS）
    - **基本思想**：从图的某个起始节点开始，首先访问起始节点，然后访问它的所有邻居节点，接着再依次访问这些邻居节点的邻居节点，以此类推，按照“层”的顺序，一层一层地进行遍历，直到遍历完所有可达节点或满足特定条件。由于是按层遍历，BFS常用于寻找无权图中两个节点之间的最短路径。
    - **实现方式**：通常借助队列（Queue）数据结构来实现。将起始节点加入队列，然后不断从队列中取出节点进行访问，并将该节点的未访问邻居节点加入队列，重复这个过程，直到队列为空。
    - **示例代码**：

    ```python
    from collections import deque

    # 以邻接表表示的图
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    def bfs(graph, start):
        visited = set()  # 用于记录已访问的节点
        queue = deque([start])  # 创建队列并将起始节点加入
        visited.add(start)

        while queue:
            node = queue.popleft()  # 从队列头部取出节点
            print(node)  # 处理节点，这里简单打印

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)  # 将未访问的邻居节点加入队列
                    visited.add(neighbor)
    bfs(graph, 'A')
    ```


2. 深度优先搜索（DFS）
    - **基本思想**：从图的某个起始节点开始，沿着一条路径尽可能深地探索下去，直到无法继续（比如到达叶子节点或已访问过的节点），然后回溯到上一个节点，继续探索其他未探索的路径，直到遍历完所有可达节点或满足特定条件。DFS有递归和非递归（使用栈实现）两种常见方式。
    - **实现方式**：
        - **递归方式**：通过递归函数不断调用自身来深入访问邻居节点，系统会自动管理调用栈。
        - **非递归方式**：手动使用栈来模拟递归过程，将节点压入栈中，然后弹出并访问，再将其未访问的邻居节点压入栈，重复操作。
    - **示例代码**：

    ```python
    # 以邻接表表示的图
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # 递归实现的DFS
    def dfs_recursive(graph, node, visited=set()):
        visited.add(node)
        print(node)  # 处理节点，这里简单打印

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_recursive(graph, neighbor, visited)

    # 非递归实现的DFS
    def dfs_iterative(graph, start):
        visited = set()
        stack = [start]
        visited.add(start)

        while stack:
            node = stack.pop()  # 从栈顶取出节点
            print(node)  # 处理节点，这里简单打印

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

    dfs_recursive(graph, 'A')
    dfs_iterative(graph, 'A')

    ```


## 拓扑排序

拓扑排序是对一个有向无环图（DAG）的所有顶点进行排序，使得对于图中的任意一条有向边 `(u, v)`，在排序后的序列中，`u` 都排在 `v` 的前面。拓扑排序常用于任务调度、依赖关系分析等场景. 

```python
def topological_sort_dfs_stack(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]

# 示例图，以邻接表形式表示
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
print(topological_sort_dfs_stack(graph))
```

## 最短路

最短路问题是图论中的经典问题，旨在找到图中两个顶点之间的最短路径。以下是几种常见的最短路实现方法：

1. 迪杰斯特拉（Dijkstra）算法
    - **适用场景**：用于计算带权有向图或无向图中从一个源点到其他所有顶点的最短路径，要求图中所有边的权值非负。
    - **基本思想**：维护一个顶点集合 `S`，初始时 `S` 只包含源点 `s`。对于每个顶点 `v`，记录从 `s` 到 `v` 的当前最短距离 `d[v]`。每次从图中选择一个不在 `S` 中且 `d[v]` 最小的顶点 `u`，将其加入 `S`，并更新与 `u` 相邻的顶点的最短距离。
    - **代码示例**

    ```python
    import heapq

    def dijkstra(graph, start):
        # 初始化距离字典，将所有顶点的距离设为无穷大
        distances = {vertex: float('inf') for vertex in graph}
        # 将起始顶点的距离设为0
        distances[start] = 0
        # 优先队列，存储待处理的顶点和距离
        pq = [(0, start)]

        while pq:
            # 取出距离最小的顶点
            current_distance, current_vertex = heapq.heappop(pq)

            # 如果当前距离大于已记录的距离，跳过
            if current_distance > distances[current_vertex]:
                continue

            # 遍历当前顶点的邻居
            for neighbor, weight in graph[current_vertex].items():
                distance = current_distance + weight
                # 如果通过当前顶点到达邻居的距离更短，更新距离
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances
    ```

2. 贝尔曼 - 福特（Bellman - Ford）算法
    - **适用场景**：能处理带权有向图中存在负权边的情况，但不能处理存在负权回路的图。
    - **基本思想**：对图中的所有边进行 `n - 1` 次松弛操作（`n` 为顶点数）。每次松弛操作都尝试更新从源点到其他顶点的最短距离，通过不断迭代来逐渐逼近最短路径。
    - **代码示例**

    ```python
    def bellman_ford(graph, start):
        # 初始化距离字典，将所有顶点的距离设为无穷大
        distances = {vertex: float('inf') for vertex in graph}
        # 将起始顶点的距离设为0
        distances[start] = 0

        # 进行|V|-1次松弛操作
        for _ in range(len(graph) - 1):
            for u in graph:
                for v, weight in graph[u].items():
                    # 如果通过u到v的距离更短，更新距离
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight

        # 检查是否存在负权回路
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    raise ValueError("图中存在负权回路")

        return distances
    ```

3. 弗洛伊德 - 沃肖尔（Floyd - Warshall）算法
    - **适用场景**：用于计算带权有向图或无向图中任意两点之间的最短路径，可处理负权边，但不能处理负权回路。
    - **基本思想**：使用动态规划的思想，通过一个二维数组 `dist` 来记录顶点之间的最短距离。初始时，`dist[i][j]` 表示直接从 `i` 到 `j` 的边的权值，如果没有直接边，则为无穷大。然后通过依次考虑每个顶点作为中间节点，来更新 `dist[i][j]` 的值。
    - **代码示例**

    ```python
    import math

    def floyd_warshall(graph):
        n = len(graph)
        # 初始化距离矩阵
        dist = [[math.inf] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    dist[i][j] = 0
                elif j in graph[i]:
                    dist[i][j] = graph[i][j]

        # 动态规划计算最短路径
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # 检查是否存在负权回路
        for i in range(n):
            if dist[i][i] < 0:
                raise ValueError("图中存在负权回路")

        return dist
    ```



## 并查集



并查集（Union-Find），也被称为不相交集合数据结构，主要用于处理不相交集合的合并与查询问题。它支持两种基本操作：

- **查找（Find）**：确定某个元素属于哪个集合，具体是通过不断查找元素的父节点，直到找到集合的代表元素（根节点）。
- **合并（Union）**：将两个不相交的集合合并成一个集合，通常是把一个集合的根节点指向另一个集合的根节点。

为了提高并查集的性能，常采用两种优化策略：

- **路径压缩**：在执行查找操作时，将元素直接连接到集合的根节点，减少后续查找的时间复杂度。
- **按秩合并**：在合并操作中，将秩（可理解为树的高度或节点数量）较小的集合合并到秩较大的集合，避免树的高度增长过快。

以下是使用 Python 实现的并查集类，包含路径压缩和按秩合并的优化：

```python
class UnionFind:
    def __init__(self, n):
        # 初始化每个元素的父节点为自身
        self.parent = list(range(n))
        # 初始化每个集合的秩为 0
        self.rank = [0] * n

    def find(self, x):
        # 查找元素 x 的根节点，并进行路径压缩
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # 找到 x 和 y 的根节点
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            # 如果 x 和 y 已经在同一个集合中，无需合并
            return

        if self.rank[root_x] < self.rank[root_y]:
            # 将秩较小的集合合并到秩较大的集合
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # 秩相等时，任选一个作为根节点，并将其秩加 1
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

    def is_connected(self, x, y):
        # 判断 x 和 y 是否在同一个集合中，即是否连通
        return self.find(x) == self.find(y)

```

1. 使用并查集判断图中两个节点是否连通

    假设图用边的列表来表示，每条边是一个包含两个节点的元组。以下是一个示例，展示如何使用上述并查集类来判断图中两个节点是否连通：

    ```python
    # 示例图的边列表
    edges = [(0, 1), (1, 2), (3, 4)]
    # 节点数量，这里假设节点编号从 0 到最大节点编号
    num_nodes = max(max(edge) for edge in edges) + 1

    # 创建并查集对象
    uf = UnionFind(num_nodes)

    # 遍历图的边，将每条边的两个节点合并到同一个集合中
    for u, v in edges:
        uf.union(u, v)

    # 判断两个节点是否连通
    node1 = 0
    node2 = 2
    print(f"节点 {node1} 和节点 {node2} 是否连通: {uf.is_connected(node1, node2)}")

    node3 = 0
    node4 = 3
    print(f"节点 {node3} 和节点 {node4} 是否连通: {uf.is_connected(node3, node4)}")

    ```


## DP



