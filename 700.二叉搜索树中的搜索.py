#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        cur = root
        while cur and cur.val != val:
            if cur.val < val:
                cur = cur.right
            else:
                cur = cur.left
        return cur

"""
Accepted
36/36 cases passed (96 ms)
Your runtime beats 21.16 % of python3 submissions
Your memory usage beats 64.4 % of python3 submissions (16.7 MB)
"""        
# @lc code=end

