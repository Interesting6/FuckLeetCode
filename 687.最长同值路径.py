# @before-stub-for-debug-begin
from python3problem687 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        res = 0
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0
            lf = dfs(node.left)
            rt = dfs(node.right)
            cur_l = cur_r = 0  #& 表示从node出发的，如果没这个，下面直接在lf/rt上操作，最后返回的cur就不是node出发的了！
            if node.left and node.left.val == node.val:  # node与左边相等，若不相等则左边路径为0
                cur_l = lf + 1
            if node.right and node.right.val == node.val:  # node与右边相等，若不相等则右边路径为0
                cur_r = rt + 1
            cur = max(cur_l, cur_r)  # 返回最长的那条边
            nonlocal res
            res = max(res, cur_l + cur_r)  # 这个时候已经包括了左=中=右、左=中、右=中、都不等，等多种情况了
            return cur

        dfs(root)
        return res


# @lc code=end

