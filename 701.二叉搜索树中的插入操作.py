# @before-stub-for-debug-begin
from python3problem701 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""我的"""
# class Solution:
#     def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
#         if not root:
#             root = TreeNode(val)
#             return root
#         def dfs(node):
#             if not node:
#                 return
#             if node.val < val: # 比当前节点大，放在当前节点右边
#                 if not node.right: # 右边无，直接添加
#                     node.right = TreeNode(val)
#                 else:
#                     dfs(node.right)  # 右边有节点，继续比较
#             else:              # 比当前节点小，放当前节点左边
#                 if not node.left: # 左边无节点，直接添加
#                     node.left = TreeNode(val)
#                 else:
#                     dfs(node.left)  # 左边有节点，继续比较
#         dfs(root)
#         return root

# """Accepted
# 35/35 cases passed (152 ms)
# Your runtime beats 41.77 % of python3 submissions
# Your memory usage beats 59.24 % of python3 submissions (17.1 MB) """


""" 找到对应位置的空节点，插入就完事了 """
class Solution:
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)  # 这里把添加的节点返回给上一层
        # 根据上一层与val的值比较，返回给上一层的左节点或右节点
        if root.val > val:
            root.left =  self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root
"""
Accepted
35/35 cases passed (140 ms)
Your runtime beats 88.37 % of python3 submissions
Your memory usage beats 29.8 % of python3 submissions (17.2 MB)
"""

# @lc code=end

