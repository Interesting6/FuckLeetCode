#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isLeaf(node):
    if not node.left and not node.right:
        return True
    else:
        return False

"""广度优先，遇到第一个叶子节点即返回"""
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         from collections import deque
#         queue = deque([root,])
#         depth = 0
#         while queue:
#             size = len(queue)
#             depth += 1
#             for _ in range(size):
#                 node = queue.popleft()
#                 if isLeaf(node):
#                     return depth
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#         return depth
"""
Accepted
52/52 cases passed (528 ms)
Your runtime beats 76.44 % of python3 submissions
Your memory usage beats 66.51 % of python3 submissions (51.7 MB)
"""

"""深度递归"""
class Solution:
    def minDepth(self, root):
        def dfs(node):
            if not node:
                return 0
            if not node.left and node.right:
                return 1 + dfs(node.right)
            if not node.right and node.left:
                return 1 + dfs(node.left)
            return 1 + min(dfs(node.left), dfs(node.right))
        return dfs(root)
"""
Accepted
52/52 cases passed (604 ms)
Your runtime beats 52.66 % of python3 submissions
Your memory usage beats 6.18 % of python3 submissions (57.9 MB)
"""

# @lc code=end

