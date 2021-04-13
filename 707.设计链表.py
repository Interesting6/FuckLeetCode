# @before-stub-for-debug-begin
from python3problem707 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = ListNode(0) # 虚拟头结点

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self.size-1:
            return -1
        cur = self.head
        while index >= 0:
            cur = cur.next
            index -= 1
        return cur.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        cur = self.head
        cur.next = ListNode(val, cur.next)
        self.size += 1


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return

        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        t = cur.next
        cur.next = ListNode(val, t)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:
            return
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        cur.next = cur.next.next
        self.size -= 1

"""
Accepted
59/59 cases passed (252 ms)
Your runtime beats 34.75 % of python3 submissions
Your memory usage beats 70.36 % of python3 submissions (15.5 MB)
"""

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

