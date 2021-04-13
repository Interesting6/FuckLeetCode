# @before-stub-for-debug-begin
from python3problem61 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""先跑一遍求长度，再跑一遍到k，麻烦"""
# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         length = 0
#         cur = head
#         while cur:
#             length += 1
#             cur = cur.next
#         if length == 0:
#             return head    
#         k = k % length
#         if k == 0:
#             return head
#         i = 0
#         cur = head
#         pre = None
#         while i < length-k:
#             pre = cur
#             cur = cur.next
#             i += 1
#         if pre:
#             pre.next = None
#         new_head = cur
#         while cur.next:
#             cur = cur.next
#         cur.next = head
#         return new_head

class Solution:
    # 还是得先跑一遍
    def rotateRight(self, head, k):
        if not head:
            return head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        k = k % length
        if k == 0:
            return head
        fp = head
        sp = head
        i = 0
        while i < k:
            fp = fp.next
            i += 1

        while fp.next:
            fp = fp.next
            sp = sp.next
        new_head = sp.next
        sp.next = None
        fp.next = head
        return new_head

# @lc code=end

