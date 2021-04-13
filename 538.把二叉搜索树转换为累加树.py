#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        sum_ = 0
        def dfs(node):
            nonlocal sum_
            if not node:
                return
            dfs(node.right)
            sum_ += node.val
            node.val = sum_
            dfs(node.left)
        dfs(root)
        return root
""" 右中左的中序遍历即可
Accepted
215/215 cases passed (68 ms)
Your runtime beats 94.76 % of python3 submissions
Your memory usage beats 90.73 % of python3 submissions (16.9 MB)
"""

# @lc code=end

