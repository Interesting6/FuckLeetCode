#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        cur = head
        stack = []
        res = []
        i = 0
        while cur:
            res.append(0)
            while stack:
                if stack[-1][1] < cur.val:
                    pre_i, pre_val = stack.pop()
                    res[pre_i] = cur.val
                else:
                    break
            stack.append((i, cur.val))
            cur = cur.next
            i += 1
        return res

"""
Accepted
76/76 cases passed (328 ms)
Your runtime beats 50 % of python3 submissions
Your memory usage beats 85.48 % of python3 submissions (18.8 MB)
"""
        
# @lc code=end

