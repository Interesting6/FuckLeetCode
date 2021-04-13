#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        dummy_head = ListNode(-1)
        cur = dummy_head
        curry = 0 # 进位
        while p1 and p2:
            t = p1.val+p2.val + curry
            curry, t = divmod(t, 10)
            cur.next = ListNode(t)
            p1 = p1.next
            p2 = p2.next
            cur = cur.next
        p = p1 if p1 else p2
        if p: # 还有链表没结束
            while p and curry: # 若有进位，继续加
                t = p.val + curry
                curry, t = divmod(t, 10)
                cur.next = ListNode(t)
                cur = cur.next
                p = p.next
            cur.next = p # 无进位了，直接将剩余部分加到末尾
        if curry: # p已经结束，但还有进位
            cur.next = ListNode(1)
        return dummy_head.next
        
"""
Accepted
1568/1568 cases passed (68 ms)
Your runtime beats 67.53 % of python3 submissions
Your memory usage beats 98.93 % of python3 submissions (14.6 MB)
"""
# @lc code=end

