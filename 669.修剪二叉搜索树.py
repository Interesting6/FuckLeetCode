#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""我的"""
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:  # 
            return root
        if root.val < low: # 1、当前节点比最低值都小，则其左子树肯定都小要删除，返回其右子树的修剪即可
            return self.trimBST(root.right, low, high)
        elif root.val > high: # 2、当前节点比最高值大，则其右子树肯定更大要删除，返回其左子树的修剪即可
            return self.trimBST(root.left, low, high)
        else: # low <= root.val <= hight  3、当前节点在范围内，不修剪，但其子树需要修剪
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
            return root
"""
Accepted
78/78 cases passed (60 ms)
Your runtime beats 64.29 % of python3 submissions
Your memory usage beats 14.96 % of python3 submissions (18.8 MB)
"""
# @lc code=end

