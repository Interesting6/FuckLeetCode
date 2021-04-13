# @before-stub-for-debug-begin
from python3problem783 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def minDiffInBST(self, root: TreeNode) -> int:
#         res = float("inf")
#         li = []
#         def dfs(node):
#             if not node:
#                 return None
#             nonlocal res
#             dfs(node.left)
#             if li:
#                 res = min(res, node.val-li[-1])
#             li.append(node.val)
#             dfs(node.right)

#         dfs(root)
#         # print(li)
#         return res
""" 醉了，居然这样搞就可以。。。一直想左边返回左子树的最右节点，还没搞出来
Accepted 换个简单的思路就出来了
46/46 cases passed (40 ms)
Your runtime beats 70.68 % of python3 submissions
Your memory usage beats 38.74 % of python3 submissions (15 MB)
"""

# 简化一下：
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res = float("inf")
        pre = None
        def dfs(node):
            if not node:
                return None
            nonlocal res, pre
            dfs(node.left)
            if pre:
                res = min(res, node.val-pre)
            pre = node.val # 作为上一个访问的节点
            dfs(node.right)
        dfs(root)
        return res
"""
Accepted
46/46 cases passed (32 ms)
Your runtime beats 96.3 % of python3 submissions
Your memory usage beats 41.67 % of python3 submissions (15 MB)
"""

# 换成传参的方式呢？就有点被绕晕了
# PY是不行的！！传参数从右节点结束回来的时候，pre就没了！！！
# 注意C++里写的是&是引用，是全局变量！
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res = float("inf")
        pre = None
        def dfs(node, pre):
            if not node:
                return None
            nonlocal res
            dfs(node.left, pre)
            print(pre, node.val)
            if pre is None: # 左叶子
                pre = node.val
            else: # 非左叶子
                res = min(res, node.val-pre)
                pre = node.val 
            dfs(node.right, pre)
        dfs(root, None)
        return res


# @lc code=end

