# @before-stub-for-debug-begin
from python3problem101 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 深度优先：
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         def isMirror(node1, node2):
#             # 检查两棵树是否对称：
#             #   1、根节点值相同，且2、一颗树左子树与另一颗树右子数对称
#             if not node1 and not node2: # 左右树都为空
#                 return True
#             elif not node1 or not node2: # 左为空右不为空 or 左不空右空
#                 return False
#             else:
#                 return (node1.val == node2.val) and \
#                     isMirror(node1.left, node2.right) and \
#                     isMirror(node1.right, node2.left)
#         return isMirror(root.left, root.right)

from collections import deque
# # 广度优先：
# class Solution:
#     def isSymmetric(self, root):
#         dq = [root, ]
#         while dq:
#             size = len(dq)
#             if size > 1:
#                 i = 0
#                 while i < size//2:
#                     if dq[i] and dq[-i-1]:
#                         if dq[i].val != dq[-i-1].val:
#                             return False
#                     elif dq[i] is None and dq[-i-1] is None:
#                         pass
#                     else:
#                         return False
#                     i += 1
#             for _ in range(size):
#                 node = dq.pop(0)
#                 if node:
#                     if node.left: 
#                         dq.append(node.left)
#                     else:
#                         dq.append(None)
#                     if node.right:
#                         dq.append(node.right)
#                     else:
#                         dq.append(None)
#         return True


# 21-04-01 第二次做
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        def isMirror(left, right):
            if not left and not right:
                return True
            elif left and right:
                if left.val == right.val:
                    return isMirror(left.left, right.right) and \
                        isMirror(left.right, right.left)
                else:
                    return False
            else:
                return False
        return isMirror(root.left, root.right)
"""
Accepted
194/194 cases passed (32 ms)
Your runtime beats 98.59 % of python3 submissions
Your memory usage beats 43.26 % of python3 submissions (15 MB)
"""
# @lc code=end

