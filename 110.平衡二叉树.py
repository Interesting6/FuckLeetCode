# @before-stub-for-debug-begin
from python3problem110 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        flag = True
        def dfs(node):
            if not node:
                return 0
            nonlocal flag
            left = dfs(node.left)
            right = dfs(node.right)
            if not flag: # flag=False 直接跳出
                return
            if abs(left - right) > 1:
                flag = False
                return
            else:
                return 1 + max(left, right)
        dfs(root)
        print(flag)
        return flag
"""
Accepted
228/228 cases passed (64 ms)
Your runtime beats 59.39 % of python3 submissions
Your memory usage beats 5.08 % of python3 submissions (19.9 MB)
"""

"""写的好看点"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node): # 返回节点高度，-1表示该节点的树已经不满足了
            if not node:
                return 0

            left = dfs(node.left)
            if left == -1: # 该节点的左子树已经不满足了
                return -1
            right = dfs(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1: # 不满足
                return -1
            else:
                return 1 + max(left, right)
        res = dfs(root)
        return res


# @lc code=end

