# @before-stub-for-debug-begin
from python3problem106 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        node_num = len(inorder)
        if node_num == 1: # 该节点为叶子节点了
            return TreeNode(inorder[0])
        root_val = postorder[-1]
        for i in range(node_num): # 通过中序遍历划分两颗子树
            if inorder[i] == root_val:
                break
        left_inorder = inorder[:i]    # 左子树的中序遍历
        right_inorder = inorder[i+1:] # 右子数的中序遍历
        left_postorder = postorder[:i]
        right_postorder = postorder[i:-1]
        # if left_inorder and 
        return TreeNode(root_val, 
                self.buildTree(left_inorder, left_postorder),
                self.buildTree(right_inorder, right_postorder) )

"""
Accepted
202/202 cases passed (360 ms)
Your runtime beats 8.09 % of python3 submissions
Your memory usage beats 16.14 % of python3 submissions (87.2 MB)
"""

# @lc code=end

