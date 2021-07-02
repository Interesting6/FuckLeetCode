# @before-stub-for-debug-begin
from python3problem897 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def increasingBST(self, root: TreeNode) -> TreeNode:
#         stack, node = [], root
#         pre = None
#         head = None
#         while stack or node:
#             while node:
#                 stack.append(node)
#                 node = node.left
#             node = stack.pop()
#             if not head:
#                 head = node
#                 pre = node
#             else:
#                 node.left = None
#                 pre.right = node
#                 pre = node
#             node = node.right
#         return head
"""
Accepted
37/37 cases passed (56 ms)
Your runtime beats 7.77 % of python3 submissions
Your memory usage beats 71.85 % of python3 submissions (14.8 MB)
"""        
# 中序遍历
class Solution:
    def increasingBST(self, root):
        dummy_root = TreeNode(-1)
        cur = dummy_root
        def dfs(node):
            nonlocal cur
            if not node:
                return
            dfs(node.left)
            cur.right = node
            node.left = None
            cur = node
            dfs(node.right)
        dfs(root)
        return dummy_root.right

"""
Accepted
37/37 cases passed (40 ms)
Your runtime beats 66.38 % of python3 submissions
Your memory usage beats 10.18 % of python3 submissions (15 MB)
"""

# @lc code=end

