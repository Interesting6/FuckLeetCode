# @before-stub-for-debug-begin
from python3problem513 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        max_dpt = 0
        res = 0
        def dfs(node, dep):
            nonlocal max_dpt, res
            if not node.left and not node.right:
                if dep > max_dpt:
                    res = node.val
                    max_dpt = dep
            if node.left:
                dfs(node.left, dep+1)
            if node.right:
                dfs(node.right, dep+1)
        dfs(root, 1)
        # print(res)
        return res
"""  li装到达最深层时的元素、深度增加时重置li法
Accepted
76/76 cases passed (52 ms)
Your runtime beats 72.64 % of python3 submissions
Your memory usage beats 11.83 % of python3 submissions (17.8 MB)
"""

"""  res更新形式
Accepted
76/76 cases passed (60 ms)
Your runtime beats 29.17 % of python3 submissions
Your memory usage beats 11.83 % of python3 submissions (17.8 MB)
"""

# @lc code=end

