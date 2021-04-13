#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node):
            if not node:
                return 
            nonlocal res
            res += 1

            dfs(node.left)
            dfs(node.right)
        dfs(root)    
        return res
"""
Accepted
18/18 cases passed (96 ms)
Your runtime beats 40.48 % of python3 submissions
Your memory usage beats 50.98 % of python3 submissions (21.6 MB)
"""

# @lc code=end

