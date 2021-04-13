# @before-stub-for-debug-begin
from python3problem92 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        cur = head
        idx = 1
        pre = None # left之前的链
        while idx != left and cur:
            pre = cur
            cur = cur.next
            idx += 1
        pre2 = None # 进入left，储存上一个访问的节点/非cur之前的节点
        while idx != right + 1:
            if idx == left:
                lf = cur # 保存left到right中的第一个
            t = cur.next
            cur.next = pre2
            pre2 = cur
            cur = t
            idx += 1
        # 退出while循环后，cur指向right后的第一个
        lf.next = cur # 将right后的链连接到反转的right-left-后面
        if pre: # left前面有链
            pre.next = pre2
            return head
        else:  # left前面无链
            return pre2
"""
Accepted
44/44 cases passed (36 ms)
Your runtime beats 83.68 % of python3 submissions
Your memory usage beats 43.88 % of python3 submissions (15 MB)
"""

# @lc code=end

