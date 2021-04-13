#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        dummy_head = ListNode(-1)
        cur = dummy_head
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        # while cur1:
        #     cur.next = cur1
        #     cur1 = cur1.next
        #     cur = cur.next
        # while cur2:
        #     cur.next = cur2
        #     cur2 = cur2.next
        #     cur = cur.next
        cur.next = cur1 if cur1 else cur2
        return dummy_head.next
# @lc code=end

