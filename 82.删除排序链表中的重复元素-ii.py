# @before-stub-for-debug-begin
from python3problem82 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        pre = dummy_head
        sp = head
        if not head or not head.next:
            return head
        fp = head.next
        while fp:
            if sp.val != fp.val:
                pre = sp
                sp = sp.next
                fp = fp.next
            else:
                while fp and sp.val == fp.val:
                    fp = fp.next
                pre.next = fp
                if fp: # fp不为空时，继续遍历；为None时，不操作
                    sp = fp
                    fp = fp.next
        return dummy_head.next

""" 双指针
Accepted
166/166 cases passed (36 ms)
Your runtime beats 98.93 % of python3 submissions
Your memory usage beats 42.87 % of python3 submissions (14.9 MB)
"""

# @lc code=end

