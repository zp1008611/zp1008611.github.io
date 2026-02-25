# 链表

## Reference

- https://leetcode.cn/discuss/post/3142882/fen-xiang-gun-ti-dan-lian-biao-er-cha-sh-6srp/


带着问题去做下面的题目：

在什么情况下，要用到哨兵节点（dummy node）？
在什么情况下，循环条件要写 while (node != null)？什么情况下要写 while (node.next != null)？


## 1 遍历链表

1. 给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。请你返回该链表所表示数字的 十进制值. [LC1290](https://leetcode.cn/problems/convert-binary-number-in-a-linked-list-to-integer/description/)

2. 给你一个链表的头节点 head ，该链表包含由 0 分隔开的一连串整数。链表的 开端 和 末尾 的节点都满足 Node.val == 0 。对于每两个相邻的 0 ，请你将它们之间的所有节点合并成一个节点，其值是所有已合并节点的值之和。然后将所有 0 移除，修改后的链表不应该含有任何 0 。返回修改后链表的头节点 head 。[LC2181](https://leetcode.cn/problems/merge-nodes-in-between-zeros/description/)

3. 给你一个头结点为 head 的单链表和一个整数 k ，请你设计一个算法将链表分隔为 k 个连续的部分。每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 1 。这可能会导致有些部分为 null 。这 k 个部分应该按照在链表中出现的顺序排列，并且排在前面的部分的长度应该大于或等于排在后面的长度。返回一个由上述 k 部分组成的数组。[LC725](https://leetcode.cn/problems/split-linked-list-in-parts/description/)


## 2 删除节点


对于单链表 `A->B->C` 来说，要删除节点 `B` 需要用到它的上一个节点 `A`，只要把 `A` 的下一个节点指向改为指向 `C`即可.  

如果需要删除头节点（`head`），那么最好是创建 `dummy node`，`dummy node`的下一个节点指向头节点. 

如果要遍历到最后一个节点，需要写 `while node`；如果要遍历到倒数第二个节点，需要写 `while node.next`。



1. 有一个单链表的 head，我们想删除它其中的一个节点 node。给你一个需要删除的节点 node 。你将 无法访问 第一个节点  head。链表的所有值都是 唯一的，并且保证给定的节点 node 不是链表中的最后一个节点。删除给定的节点。注意，删除节点并不是指从内存中删除它。这里的意思是：给定节点的值不应该存在于链表中。链表中的节点数应该减少 1。node 前面的所有值顺序相同。node 后面的所有值顺序相同。[LC237](https://leetcode.cn/problems/delete-node-in-a-linked-list/description/)

2. 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。[LC19](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/)

3. 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。[LC83](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/)


4. 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。[LC82](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/)


5. 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。[LC203](https://leetcode.cn/problems/remove-linked-list-elements/description/)

6. 给你一个整数数组 nums 和一个链表的头节点 head。从链表中移除所有存在于 nums 中的节点后，返回修改后的链表的头节点。[LC3217](https://leetcode.cn/problems/delete-nodes-from-linked-list-present-in-array/description/)

7. 给你一个链表的头节点 head 。移除每个右侧有一个更大数值的节点。返回修改后链表的头节点 head 。[LC2487](https://leetcode.cn/problems/remove-nodes-from-linked-list/description/)

8. 给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。请你将 list1 中下标从 a 到 b 的全部节点都删除，并将list2 接在被删除节点的位置。请你返回结果链表的头指针。[LC1669](https://leetcode.cn/problems/merge-in-between-linked-lists/description/)