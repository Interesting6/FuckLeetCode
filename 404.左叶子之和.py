# @before-stub-for-debug-begin
from python3problem404 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum_ = 0
        def dfs(node, dir):
            nonlocal sum_
            if not node:
                return
            if not node.left and not node.right and dir=="left":
                sum_ += node.val
            if node.left:
                dfs(node.left, "left")
            if node.right:
                dfs(node.right, "right")
        dfs(root, '')
        # print(sum_)
        return sum_
"""
Accepted
102/102 cases passed (48 ms)
Your runtime beats 23.38 % of python3 submissions
Your memory usage beats 12.61 % of python3 submissions (15.8 MB)
"""
# @lc code=end

