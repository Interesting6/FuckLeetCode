#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
#         res = []
#         stack = [ ]
#         node = root

#         while stack or node:
#             while node:
#                 stack.append(node.left)
#                 node = node.left
#             node = stack.pop()
#             res.append(node.val)
#             node = node.right
#         return res
            
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root:
#             return []
#         res = []
#         stack = [ ]
#         cur = root # 访问的指针
#         while cur or stack:
#             if cur: # 指针来访问节点，直到最底层
#                 stack.append(cur)
#                 cur = cur.left      # 左
#             else: # 访问的节点为空了
#                 cur = stack.pop()   # 从栈里弹出数据，就是要处理的数据
#                 res.append(cur.val) # 中
#                 cur = cur.right     # 右
#         return res

"""
Accepted
68/68 cases passed (48 ms)
Your runtime beats 11.02 % of python3 submissions
Your memory usage beats 84.39 % of python3 submissions (14.6 MB)
""" 

class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

# @lc code=end

