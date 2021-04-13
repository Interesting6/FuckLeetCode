# @before-stub-for-debug-begin
from python3problem236 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""深度优先递归"""
# 储存父节点
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         res = []
#         visited = set()
#         def dfsp(node, tar, path_):
#             path_.append(node.val)
#             visited.add(node)
#             if node.val == tar.val:
#                 res.append(path_.copy())
#                 return True # 找到了
#             else:
#                 if node.left and node.left not in visited:
#                     if dfsp(node.left, tar, path_):
#                         return True # 找到了直接退出，不进行后续的
#                 if node.right and node.right not in visited:
#                     if dfsp(node.right, tar, path_):
#                         return True # 找到了直接退出
#                 path_.pop() # 回溯
#         dfsp(root, p, []) # 找出p的路径
#         dfsp(root, q, []) # 找出q的路径
#         num = root
#         for i, j in zip(res[0], res[1]): # 两个路径对比可得结果
#             if i.val != j.val:
#                 break
#             else:
#                 num = i
#         return num
"""
Accepted
31/31 cases passed (96 ms)
Your runtime beats 20.4 % of python3 submissions
Your memory usage beats 5.04 % of python3 submissions (31 MB)
"""

"""官方递归"""
# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         father = None
#         def dfs(node, p, q):
#             nonlocal father
#             if not node:
#                 return False
#             inCur = (node.val == p.val) or (node.val == q.val)
#             inL = dfs(node.left, p, q) # 当前节点左子树包含p或q
#             inR = dfs(node.right, p, q) # 当前节点右子树包含p或q
#             if inL and inR: # 当前节点的左子树包含p或q，右子树也包含p或q
#                 father = node
#             if inCur and (inL or inR):
#                 father = node
#             # 返回当前节点中的子树是否包含p或q
#             return l or r or inCur
#         dfs(root, p, q)
#         return father

# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         """若p和q 在root的子树两侧，就返回该节点；
#         若在该子树的一侧，则返回该侧的子节点；
#         否者返回None"""
#         if not root or root.val == p.val or root.val == q.val: # 终止条件
#             return root

#         left = self.lowestCommonAncestor(root.left, p, q)
#         right = self.lowestCommonAncestor(root.right, p, q)

#         if not left and not right: # 情况1：既不在左、也不再右，可以合并到情况2、3中，
#             return    # 因为返回另一方，另一方也是None
#         if not left:  # 情况3：不在该节点左子树中，则在其右子树中
#             return right
#         if not right: # 情况4：不在该节点右子树中，则在其左子树中
#             return left

#         if left and right: # 情况2：一个在左一个在右，必然当前节点就是其最近公共祖先
#             return root # 返回当前，而不是返回子节点


# 3.28 第二次做
# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         def dfs(node, p, q):
#             if not node or node.val==p.val or node.val == q.val:
#                 return node
#             left = dfs(node.left, p, q)
#             right = dfs(node.right, p, q)
#             if left and right: # 一个在左边一个在右边
#                 return node
#             if not left and right:
#                 return right
#             if not right and left:
#                 return left
#             if not left and not right:
#                 return None
#         res = dfs(root, p, q)
#         return res
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        father = None
        def dfs(node, p, q):
            nonlocal father
            if not node:
                return False
            incur = node.val==p.val or node.val == q.val
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            if left and right: # 一个在左边一个在右边
                father = node
            if incur and (left or right):
                father = node
            return left or right or incur # 返回p或q在该颗树上
        dfs(root, p, q)
        return father

# @lc code=end

