#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""DFS"""
# class Solution:
#     def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
#         x_parent, x_dep, x_find = None, None, False
#         y_parent, y_dep, y_find = None, None, False
#         def dfs(node, dep, parent):
#             nonlocal x_parent, x_dep, x_find
#             nonlocal y_parent, y_dep, y_find
#             if not node:
#                 return -1
#             if node.val == x:
#                 x_parent, x_dep, x_find = parent, dep, True
#             elif node.val == y:
#                 y_parent, y_dep, y_find = parent, dep, True
#             if x_find and y_find: # x, y都找到了
#                 return
#             dfs(node.left, dep+1, node)
#             if x_find and y_find: # 再次剪枝 x, y都找到了
#                 return
#             dfs(node.right, dep+1, node)
            
#         dfs(root, 0, root)
#         if x_dep == y_dep and x_parent != y_parent:
#             return True
#         else:
#             return False

""" DFS
Accepted
104/104 cases passed (32 ms)
Your runtime beats 98.81 % of python3 submissions
Your memory usage beats 96.82 % of python3 submissions (14.6 MB)
"""


# 试试BFS：
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        from collections import deque
        dq = deque([(root, None)])
        x_find, y_find = False, False
        x_parent, y_parent = None, None
        while dq:
            size = len(dq)
            next_layer = []
            for _ in range(size):
                node, parent = dq.popleft()
                if node.val == x:
                    x_find = True
                    x_parent = parent
                elif node.val == y:
                    y_find = True
                    y_parent = parent
                if node.left:
                    next_layer.append((node.left, node))
                if node.right:
                    next_layer.append((node.right, node))
            if x_find and y_find: # 这时候x、y同深度
                if x_parent == y_parent: # 亲兄弟
                    return False 
                else:
                    return True # 堂兄弟
            elif x_find or y_find: # 在该深度只有一个找到
                return False
            else: # 该深度都没找到，继续向下一层
                dq.extend(next_layer)

"""
Accepted
104/104 cases passed (44 ms)
Your runtime beats 53.28 % of python3 submissions
Your memory usage beats 43.14 % of python3 submissions (14.9 MB)
"""

        
# @lc code=end

