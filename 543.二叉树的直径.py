#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal res
            left = dfs(node.left)
            right = dfs(node.right)
            mx = max(left, right)
            res = max(res, left + right)
            return mx + 1
        dfs(root)
        return res
""" 居然秒了，学了lc124后，这个题容易多了
Accepted
104/104 cases passed (52 ms)
Your runtime beats 77.09 % of python3 submissions
Your memory usage beats 54.84 % of python3 submissions (16.8 MB)
"""
# @lc code=end

