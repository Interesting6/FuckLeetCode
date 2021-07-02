# @before-stub-for-debug-begin
from python3problem145 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
#         stack, cur = [], root
#         res = []
#         pre = None # 上一个处理的节点
#         while stack or cur:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.left
#             cur = stack.pop()
#             if not cur.right or cur.right == pre:
#                 # 处理节点
#                 res.append(cur.val)
#                 pre = cur
#                 cur = None
#             else:
#                 stack.append(cur)
#                 cur = cur.right
#         return res

# 2021-05-17
class Solution:
    def postorderTraversal(self, root):
        res = []
        stack, cur = [], root
        pre = None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.right and cur.right != pre:
                stack.append(cur)
                cur = cur.right
            else:
                res.append(cur.val)
                pre = cur
                cur = None

        return res

# 测试用例[1, 2, 3, 4, 5, null, 6, null, null, 7, 8]
"""
Accepted 不枉我做了这么久
68/68 cases passed (40 ms)
Your runtime beats 61.61 % of python3 submissions
Your memory usage beats 12.06 % of python3 submissions (14.9 MB)
"""


# @lc code=end

