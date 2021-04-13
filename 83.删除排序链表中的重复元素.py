#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(-101)
        dummy_head.next = head
        cur = head
        pre = dummy_head
        while cur:
            if cur.val == pre.val: # 当前值与上一个相等
                if not cur.next: # 连续的结尾
                    pre.next = None
                cur = cur.next # 下一个
            else:
                pre.next = cur # 当前与上一个不相等，接上去
                pre = cur
                cur = cur.next
        return dummy_head.next

"""
Accepted
165/165 cases passed (40 ms)
Your runtime beats 95.13 % of python3 submissions
Your memory usage beats 87.77 % of python3 submissions (14.8 MB)
"""

# @lc code=end

