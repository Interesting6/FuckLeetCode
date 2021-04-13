# @before-stub-for-debug-begin
from python3problem19 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        fp = dummy
        sp = dummy
        while n > 0:
            fp = fp.next
            n -= 1
        while fp.next:
            fp = fp.next
            sp = sp.next
        sp.next = sp.next.next
        return dummy.next
"""
Accepted
208/208 cases passed (40 ms)
Your runtime beats 74.89 % of python3 submissions
Your memory usage beats 78.76 % of python3 submissions (14.7 MB)
"""
# @lc code=end

