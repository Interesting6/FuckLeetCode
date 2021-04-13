# @before-stub-for-debug-begin
from python3problem116 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""广度优先"""
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root:
#             return root
#         queue = [root, ]
#         while queue:
#             size = len(queue)
#             if size == 1:
#                 node = queue.pop()
#                 node.next = None
#                 if node.left:
#                     queue.append(node.left)
#                     queue.append(node.right)
#             else:
#                 li = []
#                 queue.append(None)
#                 for i in range(size):
#                     queue[i].next = queue[i+1]
#                     if queue[i].left:
#                         li.append(queue[i].left)
#                     if queue[i].right:
#                         li.append(queue[i].right)
#                 queue = li
#         return root

# 递归深度
class Solution:
    def connect(self, root):
        if not root:
            return root

        def DFS(node): # 将该子树的两个节点的邻居连接起来
            if not node:
                return None
            if node.left and node.right:
                # 对于左节点
                node.left.next = node.right # 先将两个子节点连接起来
                # 对于右子节点，
                if node.next: # 若当前节点有邻居，则连接邻居的左子节点
                    node.right.next = node.next.left
                else: # 否者是最右边的节点，直接连none
                    node.right.next = None
                # 然后分别对左子树 和右子树分别进行。
                DFS(node.left) 
                DFS(node.right)
            return node
        root.next = None # 根节点初始化
        return DFS(root)
"""
Accepted
58/58 cases passed (84 ms)
Your runtime beats 39.77 % of python3 submissions
Your memory usage beats 80.14 % of python3 submissions (16.2 MB)
"""

# @lc code=end

