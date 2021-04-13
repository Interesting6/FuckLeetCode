# @before-stub-for-debug-begin
from python3problem98 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""中序遍历，结果有序法"""
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         li = []
#         def inorder(node):
#             if node.left:
#                 inorder(node.left)
#             li.append(node.val)
#             if node.right:
#                 inorder(node.right)
#         inorder(root)
#         n = len(li)
#         for i in range(1, n):
#             if li[i-1] >= li[i]:
#                 return False
#         return True
"""
Accepted
77/77 cases passed (60 ms)
Your runtime beats 30.58 % of python3 submissions
Your memory usage beats 5.47 % of python3 submissions (17.9 MB)
"""

# """每个节点都用一个上下界限制，递归时左边节点的上界更新为当前节点，右边节点下界更新为当前节点"""
# class Solution:
#     def isValidBST(self, root):
#         def dfs(node, lower, upper):
#             if not node:
#                 return True
#             if lower < node.val < upper:  # 当前节点在上下界内
#                 l = dfs(node.left, lower, node.val) # 左边节点递归时更新上界为当前点
#                 r = dfs(node.right, node.val, upper)# 右边节点递归时更新下界为当前点
#                 return l and r
#             else:
#                 return False
#         return dfs(root, -float("inf"), float("inf"))

# """
# Accepted
# 77/77 cases passed (52 ms)
# Your runtime beats 74.63 % of python3 submissions
# Your memory usage beats 37.41 % of python3 submissions (17.3 MB)
# """

"""中序遍历顺利法"""
# 维护一个递增的最小值
class Solution:
    def isValidBST(self, root):
        minv = -float("inf")
        def dfs(node):
            nonlocal minv
            if not node:
                return True
            l = dfs(node.left)
            # 进入最左边了才第一次执行下面语句，左边结束后跳出回溯到其父节点又执行下面的语句
            if minv < node.val:
                minv = node.val
            else:
                return False
            r = dfs(node.right) # 上面语句结束了再执行父节点的右儿子，画个图出来好理解
            return l and r
        return dfs(root)
"""
Accepted
77/77 cases passed (56 ms)
Your runtime beats 53.13 % of python3 submissions
Your memory usage beats 13.76 % of python3 submissions (17.8 MB)
"""

# @lc code=end

