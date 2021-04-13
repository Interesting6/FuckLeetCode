# @before-stub-for-debug-begin
from python3problem230 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cnt = 0
        res = 0
        def dfs(node):
            nonlocal cnt, res
            if not node:
                return
            if node.left:
                dfs(node.left)
            if cnt == k-1:
                res = node.val
                cnt += 1
                return
            elif cnt > k-1:
                return
            else:
                cnt += 1
            if node.right:
                dfs(node.right)
        dfs(root)
        return res

""" 抓住中序是有序的就行
Accepted
93/93 cases passed (52 ms)
Your runtime beats 94.01 % of python3 submissions
Your memory usage beats 29.36 % of python3 submissions (18.7 MB)"""
# @lc code=end

