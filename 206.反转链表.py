# @before-stub-for-debug-begin
from python3problem206 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            t = cur.next # 保存当前下一个节点的值
            cur.next = pre # 重新指向反方向，翻转操作
            pre = cur    # 更新前一个的值和下一个指针
            cur = t
        return pre



# @lc code=end

