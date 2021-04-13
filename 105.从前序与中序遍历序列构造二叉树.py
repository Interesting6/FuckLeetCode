#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        n = len(inorder)
        for i in range(n):
            if inorder[i] == preorder[0]:
                break
        node.left = self.buildTree(preorder[1:1+i], inorder[:i])
        node.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return node


# @lc code=end

