# @before-stub-for-debug-begin
from python3problem501 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        res = []
        max_cnt = 1 # 初始化为第一个节点，最大频率
        cnt = 1     # 初始化为第一个节点，当前数字频率
        pre = None
        def dfs(node):
            nonlocal res, cnt, pre, max_cnt
            if not node:
                return
            dfs(node.left)
            if pre:
                if node.val == pre.val:
                    cnt += 1
                else:
                    cnt = 1
                if cnt > max_cnt: # 出现的次数更多了
                    max_cnt = cnt
                    res.clear() # 将之前收集的众数清楚
                    res.append(node.val)
                elif cnt == max_cnt: # 不同的众数
                    res.append(node.val)
            else: # 第一个节点
                res.append(node.val)
            pre = node
            dfs(node.right)
        dfs(root)
        return res
"""
Accepted
25/25 cases passed (72 ms)
Your runtime beats 37.38 % of python3 submissions
Your memory usage beats 86.65 % of python3 submissions (18.3 MB)
"""
# @lc code=end

