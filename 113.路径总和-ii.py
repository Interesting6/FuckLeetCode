# @before-stub-for-debug-begin
from python3problem113 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
广度优先
"""
# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
#         res = []
#         def bfs(node):
#             if not node:
#                 return []
#             queue = [([], 0, node)]
#             while queue:
#                 path_, sum_, node = queue.pop(0)
#                 sum_ = sum_ + node.val
#                 path_ = path_.copy() # 保存节点路径
#                 path_.append(node.val)
#                 if not node.left and not node.right:
#                     if sum_ == sum:
#                         res.append(path_)
#                 else:
#                     if node.left:
#                         queue.append((path_, sum_, node.left))
#                     if node.right:
#                         queue.append((path_, sum_, node.right))
#         bfs(root)
#         return res

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        path = []
        if not root:
            return res

        def recur(root, tar):
            path.append(root.val) # 加入路径
            tar = tar - root.val # 目标减少
            if not root.left and not root.right: # 叶子节点
                if tar == 0: # 找到目标值
                    res.append(path.copy())
            if root.left: 
                recur(root.left, tar)
            if root.right:
                recur(root.right, tar)
            path.pop() # node有子节点时，当两个*子节点*递归都结束时，向上回溯，把该节点删除
            # 或者是node是叶子节点时，上面俩if不执行，退出recur时，回到上一个节点前，把该点从路径删除
        recur(root, targetSum)
        return res

"""
Accepted
115/115 cases passed (44 ms)
Your runtime beats 92.27 % of python3 submissions
Your memory usage beats 51.49 % of python3 submissions (16.1 MB)
"""

# @lc code=end

