# @before-stub-for-debug-begin
from python3problem102 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        li = []
        if not root:
            return li
        def dfs(index, node):
            if not node: return
            if index+1 > len(li): # li里需要的框数 大于 li里实际的框数时，需要加框
                li.append([])
            li[index].append(node.val)
            dfs(index+1, node.left)
            dfs(index+1, node.right)
        dfs(0, root)
        # print(li)
        return li
# @lc code=end

