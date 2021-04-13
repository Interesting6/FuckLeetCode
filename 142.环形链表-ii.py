#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # 快慢指针相遇
                p = head # 一个从头开始走
                while p != slow:  # 一个从相遇的地方开始走，肯定在入口处相遇
                    p = p.next
                    slow = slow.next
                return p
        return None
"""
由数学推出，链表开始环入口的距离 等于 相遇处到入口处的距离+k个环的大小
则只要在相遇处出发一个点，肯定能与链表开始处出发的一个点，在环入口处相遇
Accepted
16/16 cases passed (56 ms)
Your runtime beats 81.86 % of python3 submissions
Your memory usage beats 22.95 % of python3 submissions (17.9 MB)
"""
# @lc code=end

