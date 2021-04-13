# @before-stub-for-debug-begin
from python3problem257 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 显示回溯
# class Solution:
#     def binaryTreePaths(self, root: TreeNode) -> List[str]:
#         res = []
#         li = []
#         if not root:
#             return res
#         def dfs(node):
#             li.append(str(node.val))
#             if not node.left and not node.right:
#                 res.append("->".join(li))
#                 return
#             if node.left:
#                 dfs(node.left)
#                 li.pop()   # 回溯
#             if node.right:
#                 dfs(node.right)
#                 li.pop()   # 回溯
#         dfs(root)
#         # print(res)
#         return res
# """
# 执行用时：48 ms, 在所有 Python3 提交中击败了17.68%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了34.62%的用户
# """

class Solution:
    def binaryTreePaths(self, root):
        res = []
        def dfs(node, pth):
            if node:
                pth += str(node.val)
                if not node.left and not node.right:
                    res.append(pth)
                pth += "->"
                if node.left:
                    dfs(node.left, pth) 
                    # 这个函数退出后，pth还是上面那个pth，因为str是不可变对象，
                    # 虽然在这个递归函数里实参pth看起来改变了，但函数外的实际pth并未变
                    # 达到了一种回溯的效果
                if node.right:
                    dfs(node.right, pth)
        dfs(root, '')
        print(res)
        return res

# @lc code=end

