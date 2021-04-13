#
# @lc app=leetcode.cn id=1669 lang=python3
#
# [1669] 合并两个链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy_head = ListNode(-1)
        dummy_head.next = list1
        cur1 = dummy_head
        cur2 = list2
        i = 0
        for j in range(a):
            cur1 = cur1.next
        l1_tail = cur1
        for j in range(b-a+2):
            cur1 = cur1.next
        l1_head = cur1
        l1_tail.next = list2
        while cur2.next:
            cur2 = cur2.next
        cur2.next = l1_head
        return dummy_head.next

# @lc code=end

