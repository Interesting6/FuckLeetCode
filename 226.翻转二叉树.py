#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return root
#         def dfs(node):
#             if not node:
#                 return
#             node.left, node.right = node.right, node.left
#             if node.left:
#                 dfs(node.left)
#             if node.right:
#                 dfs(node.right)
#         dfs(root)
#         return root
"""
Accepted
68/68 cases passed (36 ms)
Your runtime beats 82.24 % of python3 submissions
Your memory usage beats 48.33 % of python3 submissions (14.8 MB)
"""


# 21-04-05 第二次做
class Solution:
    def invertTree(self, root):
        def dfs(node):
            if not node:
                return
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            node.left, node.right = node.right, node.left
        dfs(root)
        return root
            
# @lc code=end

