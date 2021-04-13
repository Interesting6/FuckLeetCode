# @before-stub-for-debug-begin
from python3problem234 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         stack = []
#         cur = head
#         i = 0
#         while cur:
#             stack.append(cur.val)
#             cur = cur.next
#         n = len(stack)
#         for i in range(n//2):
#             if stack[i] != stack[n-1-i]:
#                 return False
#         return True
"""
找到中间节点，断开，并翻转后面的链表
"""
class Solution:
    def isPalindrome(self, head):
        sp = head
        fp = head
        i = 0
        # 找中点
        pre = None
        while fp.next:
            fp = fp.next
            if fp.next:
                fp = fp.next
            pre = sp
            sp = sp.next
            i += 1

        if pre is None: # 只有一个节点
            return True

        pre.next = None # 截断
        cur = sp # 指向第二条，并反转第二条
        pre = None
        while cur:
            t = cur.next
            cur.next = pre
            pre = cur
            cur = t
        # 开始两个链表比较
        cur1 = head # 第一条
        cur2 = pre # 第二条
        while cur1 and cur2:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return True

# @lc code=end

