# @before-stub-for-debug-begin
from python3problem654 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        n = len(nums)
        max_ = -1
        idx = -1
        for i in range(n):
            if nums[i] > max_:
                max_ = nums[i]
                idx = i
        node = TreeNode(nums[idx])
        node.left = self.constructMaximumBinaryTree(nums[:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return node
"""
Accepted
107/107 cases passed (148 ms)
Your runtime beats 49.65 % of python3 submissions
Your memory usage beats 62.84 % of python3 submissions (15.3 MB)
"""
# @lc code=end

