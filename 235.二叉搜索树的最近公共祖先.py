# @before-stub-for-debug-begin
from python3problem235 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_ = min(p.val, q.val)
        q_ = max(p.val, q.val)
        def dfs(node):
            if not node:
                return None
            if p_ <= node.val <= q_:
                return node
            l = dfs(node.left) # 类似于最近公共祖先的写法。
            r = dfs(node.right)
            if l:
                return l
            if r:
                return r
        return dfs(root)
"""
Accepted
27/27 cases passed (80 ms)
Your runtime beats 91.86 % of python3 submissions
Your memory usage beats 59.69 % of python3 submissions (18.8 MB)
"""


# @lc code=end

