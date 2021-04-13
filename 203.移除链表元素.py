#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
#         if not head:
#             return head
#         while head and head.val == val: # 若在头部出现，就先把头部的去掉
#             head = head.next
#         cur = head
#         while cur:
#             if cur.val == val:
#                 pre.next = cur.next # 将当前点的next接到前一个点next上
#             else: # 这个时候头部不为val，则pre会被赋值
#                 pre = cur
#             cur = cur.next # 指向下一个
#         return head
"""
Accepted
66/66 cases passed (76 ms)
Your runtime beats 40.97 % of python3 submissions
Your memory usage beats 33.48 % of python3 submissions (17.9 MB)
Accepted 两段差不多的代码，百分比相差好大。
66/66 cases passed (64 ms)
Your runtime beats 90.87 % of python3 submissions
Your memory usage beats 58.59 % of python3 submissions (17.8 MB)
"""

"""从上面可以知道，若头结点元素出现时，处理逻辑跟后面的节点的处理逻辑不同
这个时候，引入一个虚拟头结点会比较方便"""
class Solution:
    def removeElements(self, head, val):
        if not head:
            return head
        dummyHead = ListNode(0, head)
        cur = dummyHead
        while cur.next:  # 注意这里的逻辑，是判断下一个节点
            if cur.next.val == val:
                cur.next = cur.next.next # 连接到下一个节点
                # 当删除一个节点时，不需要移到下一个节点，由于while里会判断下一个节点
            else:
                cur = cur.next
        head = dummyHead.next
        return head
"""
Accepted
66/66 cases passed (76 ms)
Your runtime beats 40.93 % of python3 submissions
Your memory usage beats 64.78 % of python3 submissions (17.8 MB)
"""

# @lc code=end

