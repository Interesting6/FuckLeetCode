#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            if node.val < low:
                return dfs(node.right)
            if node.val > high:
                return dfs(node.left)
            left = dfs(node.left)
            right = dfs(node.right)
            return left + right + node.val
        res = dfs(root)
        return res
"""
Accepted
41/41 cases passed (216 ms)
Your runtime beats 76.74 % of python3 submissions
Your memory usage beats 84.85 % of python3 submissions (22.9 MB)
"""

# @lc code=end

