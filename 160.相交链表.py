# @before-stub-for-debug-begin
from python3problem160 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        while pa != pb:
            pa = pa.next if pa else headB # 注意这里是headB，不是pb！
            pb = pb.next if pb else headA
        return pa

# @lc code=end

