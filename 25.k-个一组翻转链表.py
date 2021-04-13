# @before-stub-for-debug-begin
from python3problem25 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
#         import copy
#         dummy_head = ListNode(-1)
#         dummy_head.next = head
#         cur = head
#         last_tail = dummy_head
#         i = 0
#         while cur:
#             i += 1
#             if i == 1:
#                 t2 = cur  # 记录每组的第一个
#                 pre = cur
#                 cur = cur.next
#                 pre.next = None # pre只能要cur当前的一个，其next得截断。
#                 # 但其也是cur引用，即把t2也截断了。试了深拷贝，结果指针又有问题，好像完全在一个新的链表上了，与之前无关了。。。这个方案行不通呀。。
#             else: # 将一组的k个先翻转
#                 t = cur.next
#                 cur.next = pre
#                 pre = cur
#                 cur = t
#                 if i == k: # 翻转完一组，将该组的翻转后的头pre 接到上一组的尾
#                     i = 0
#                     last_tail.next = pre # 上一组的尾.next = 当前组的头(pre)
#                     last_tail = t2 # 进行下一轮做准备， 将该组的头作为上一组的尾巴
#         last_tail.next = t2  # 最后一个未满的组不翻转
#         return dummy_head.next

# class Solution:
#     def reverseKGroup(self, head, k):
#         def reverse(head, k):
#             pre = None
#             cur = head
#             i = 0
#             while cur and i < k:
#                 t = cur.next
#                 cur.next = pre
#                 pre = cur
#                 cur = t
#                 i += 1
#             return pre, head 
#             # 这个与后面的区别就是，这个k之后的数据被丢失了。而后面的那个函数k后还有原数据

#         # def reverse(head, tail):
#         #     pre = tail.next
#         #     cur = head
#         #     while pre != tail:
#         #         nex = cur.next
#         #         cur.next = pre
#         #         pre = cur
#         #         cur = nex
#         #     return tail, head  # 翻转后的结尾后还留有原信息

#         dummy_head = ListNode(-1)
#         dummy_head.next = head

#         cur = head
#         pre = dummy_head
#         while cur:
#             # 检查剩余部分是否大于k
#             sub_cur = pre
#             for _ in range(k):
#                 sub_cur = sub_cur.next
#                 if not sub_cur:  # 剩余部分小于k个，直接返回链表
#                     return dummy_head.next
#             # 否则该轮大于k个，因为从pre开始上面的循环只让sub_cur到本轮的第k个(最后)一个
#             nex = sub_cur.next # 保存下一轮的头
            
#             sub_head, sub_tail = reverse(cur, k) # 翻转该轮的子链表
#             # sub_head, sub_tail = reverse(cur, sub_cur) # 翻转该轮的子链表

#             # 把本轮子链表接到上轮尾pre与下轮头nex之间，如下可视化，->>为拼接
#             # pre ->> sub_head -> ... -> sub_tail(新pre) ->> nex
#             pre.next = sub_head 
#             sub_tail.next = nex

#             pre = sub_tail  # 本轮尾巴用于下一轮，作为上一轮的尾巴
#             cur = nex # 开始下一轮的头
#         return dummy_head.next


class Solution:
    def reverseKGroup(self, head, k):
        def reverse(head, k):
            pre = None
            cur = head
            i = 0
            while cur and i < k:
                t = cur.next
                cur.next = pre
                pre = cur
                cur = t
                i += 1
            return pre, head 

        dummy_head = ListNode(-1)
        dummy_head.next = head

        cur = head # 指向第一轮的头
        pre = dummy_head
        while cur:
            # 检查剩余部分是否大于k
            sub_cur = cur # 从当前轮第一个开始
            for i in range(k):
                sub_cur = sub_cur.next
                if not sub_cur:
                    if 1+i<k:  # 剩余部分小于k个，直接返回链表
                        return dummy_head.next
                    else: # 否者刚刚好够k个，进行下面的操作
                        pass
            # 否则该轮大于k个，结束for后，sub_cur移动到下一轮的开头

            sub_head, sub_tail = reverse(cur, k) # 翻转该轮的子链表
            # 把本轮子链表接到上轮尾pre与下轮头sub_cur之间，如下可视化过程，->>为拼接
            # pre(上一轮尾) ->> sub_head -> ... -> sub_tail ->> sub_cur(下一轮头)
            pre.next = sub_head 
            sub_tail.next = sub_cur

            pre = sub_tail  # 将本轮尾巴用于下一轮，作为上一轮的尾巴
            cur = sub_cur # 开始下一轮的头
            # pre(上一轮尾) ->> sub_head -> ... -> sub_tail(新的pre) ->> sub_cur(新的cur)
        return dummy_head.next

"""
Accepted
62/62 cases passed (44 ms)
Your runtime beats 96.52 % of python3 submissions
Your memory usage beats 47.76 % of python3 submissions (15.6 MB)
"""

# @lc code=end

