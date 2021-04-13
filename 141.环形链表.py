#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""直接标记法"""
# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         while head:
#             if head.val == "vis":
#                 return True
#             else:
#                 head.val = "vis"
#             head = head.next
#         return False
"""
Accepted
19/19 cases passed (52 ms)
Your runtime beats 93.49 % of python3 submissions
Your memory usage beats 88.24 % of python3 submissions (17.7 MB)
"""  

"""双指针法"""
class Solution:
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            if fast == slow:
                return True
            slow = slow.next
        return False
"""
Accepted
19/19 cases passed (68 ms)
Your runtime beats 31.88 % of python3 submissions
Your memory usage beats 56.06 % of python3 submissions (17.9 MB)
"""
# @lc code=end

