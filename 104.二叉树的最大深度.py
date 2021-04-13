#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         res = 0 # 当前最大层
#         def DFS(node, dep): # node为当前节点， dep为该node所在层数
#             nonlocal res
#             if node is None: # 为空则啥也不进行
#                 return
#             if node.left or node.right: # 存在子节点
#                 DFS(node.left, dep+1)
#                 DFS(node.right, dep+1)
#             else: # 是叶子节点
#                 res = max(dep, res) # 当前节点所在层数与最大层比较，取最大值
#         DFS(root, 1)
#         return res

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:

#         def DFS(node): # node为当前节点，返回该节点构成的数的层数，有点自底向上的意思
#             nonlocal res
#             if node is None: # 为空节点
#                 return 0
#             # 返回当前树的左子树与右子树中更大的那个+1
#             return 1 + max(DFS(node.left), DFS(node.right)) 
#         res = DFS(root)
#         return res
# """
# 40ms
# """

# 广度优先搜索
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        dq = deque([root, ])
        res = 0
        while dq:
            size = len(dq)
            res += 1
            for _ in range(size):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return res

"""
Accepted
39/39 cases passed (48 ms)
Your runtime beats 75.53 % of python3 submissions
Your memory usage beats 78.85 % of python3 submissions (15.8 MB)
"""


# @lc code=end

