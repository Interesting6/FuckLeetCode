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

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         if not headA or not headB:
#             return None
#         pa = headA
#         pb = headB
#         while pa != pb:
#             pa = pa.next if pa else headB # 注意这里是headB，不是pb！
#             pb = pb.next if pb else headA
#         return pa
"""注意这里是if pa，这样的话pa可以取到链表最后的None值；如果是if pa.next的话，pa就取不到最后的None值了
所以在不相交的时候，可以跳出，返回none
所以目的就是让指针能先指向None，在下一步再去指另一条链表。
"""

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        curA = headA
        curB = headB
        flagA = 0
        flagB = 0
        while curA != curB:
            curA = curA.next
            curB = curB.next
            if not curA:
                curA = headB
                flagA += 1
            if not curB: # 这里不能是elif，否者会出现curA和curB都为null，这部跳过到下一个循环时，b无next
                curB = headA
                flagB += 1
            if flagA == 2 or flagB == 2:
                return 
        return curA
""" 这里用了个计数的法则，都遍历了两次后就认为不相交了。。。
Accepted
39/39 cases passed (208 ms)
Your runtime beats 9.05 % of python3 submissions
Your memory usage beats 90.19 % of python3 submissions (29.5 MB)
"""     

# @lc code=end

