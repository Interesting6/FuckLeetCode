#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""解题思路：寻找中间的点作为根节点，左节点由左边数组递归，右节点由右边递归"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n < 1:
            return None
        mid = n // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node

"""
Accepted
31/31 cases passed (48 ms)
Your runtime beats 88.61 % of python3 submissions
Your memory usage beats 81.84 % of python3 submissions (16.1 MB)
"""
# @lc code=end

