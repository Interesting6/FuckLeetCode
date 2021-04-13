#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
        elif root1 and not root2: # 如果root1为空，则合并后即为root2
            return root1
        elif not root1 and root2:
            return root2
        else:
            return None
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        return node
"""
Accepted
182/182 cases passed (80 ms)
Your runtime beats 68.63 % of python3 submissions
Your memory usage beats 88.06 % of python3 submissions (15.1 MB)
"""

# @lc code=end

