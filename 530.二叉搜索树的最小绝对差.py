# @before-stub-for-debug-begin
from python3problem530 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def getMinimumDifference(self, root: TreeNode) -> int:
#         dif = float("inf")
#         li = []
#         stack = []
#         node = root
#         pre = None
#         while stack or node:
#             while node:
#                 stack.append(node)
#                 node = node.left
#             node = stack.pop()
#             if pre:
#                 dif = min(dif, node.val-pre.val)
#             pre = node
#             node = node.right
#         return dif
"""
Accepted 列表法
186/186 cases passed (64 ms)
Your runtime beats 63.15 % of python3 submissions
Your memory usage beats 76.36 % of python3 submissions (16.7 MB)
Accepted 记录上一个节点法
186/186 cases passed (56 ms)
Your runtime beats 93.9 % of python3 submissions
Your memory usage beats 77.25 % of python3 submissions (16.7 MB)
"""

# 该程序错误
# class Solution:
#     def getMinimumDifference(self, root):
#         dif = float("inf")
#         def dfs(node, pre):
#             if not node:
#                 return 
#             nonlocal dif
#             dfs(node.left, node) 节点相连，而中序可以看到有些地方不是节点相连
#             if pre:
#                 d = node.val - pre.val # 
#                 dif = min(d, dif)
#             dfs(node.right, node)
#         dfs(root, None)
#         print(dif)
#         return dif


"""这种记录上一个节点的方法要记住！"""
# class Solution:
#     def getMinimumDifference(self, root):
#         dif = float("inf")
#         pre = None # 储存上次访问的节点
#         def dfs(node): # 当前节点处理时一定比上次访问节点大，比下次访问节点小
#             if not node:
#                 return 
#             nonlocal pre, dif
#             dfs(node.left)   # 左
#             if pre:
#                 dif = min(dif, node.val-pre.val) # 中
#             pre = node # 记录该节点为上次访问的节点
#             dfs(node.right) # 右
#         dfs(root)
#         return dif
"""Accepted
186/186 cases passed (64 ms)
Your runtime beats 63.15 % of python3 submissions
Your memory usage beats 23.38 % of python3 submissions (16.9 MB)"""
# @lc code=end

