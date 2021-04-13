# @before-stub-for-debug-begin
from python3problem337 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""暴力递归，后序遍历，超时；加记忆化"""
# class Solution:
#     di = {}
#     def rob(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         if not root.left and not root.right:
#             return root.val # 叶子节点返回当前值
#         if root in self.di:
#             return self.di[root]
#         # 偷当前节点，跳过子节点
#         val1 = root.val
#         if root.left: # 跳过左孩子；有可能存在一个子节点为None，则会报错
#             val1 += self.rob(root.left.left) + self.rob(root.left.right)
#         if root.right: # 跳过右孩子
#             val1 += self.rob(root.right.left) + self.rob(root.right.right)
#         # 不偷当前节点，偷子节点；因为不是叶子节点，故肯定有子节点
#         val2 = 0
#         val2 = self.rob(root.left) + self.rob(root.right)
#         val = max(val1, val2)
#         self.di[root] = val
#         return val
"""
Accepted
124/124 cases passed (64 ms)
Your runtime beats 41.42 % of python3 submissions
Your memory usage beats 16.12 % of python3 submissions (17.6 MB)"""


# 递归+动态规划，每个节点都返回投与不投当前节点的结果
class Solution:
    def rob(self, root):
        def f(root):
            if not root:
                return [0, 0]
            left = f(root.left)
            right = f(root.right)
            # 偷当前的，那么子节点不偷
            val1 = root.val + left[1] + right[1]
            # 不偷当前的，那么子节点偷
            # val2 = 0 + left[0] + right[0]
            # 不偷当前的，子节点可偷可不偷！而不是必须偷！
            val2 = 0 + max(left) + max(right)
            return [val1, val2] # 返回偷当前与不偷当前的结果
        res = max(f(root))
        return res

"""
Accepted
124/124 cases passed (48 ms)
Your runtime beats 97.38 % of python3 submissions
Your memory usage beats 74.53 % of python3 submissions (16.7 MB)
"""
# @lc code=end

