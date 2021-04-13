# @before-stub-for-debug-begin
from python3problem112 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 广度
# class Solution:
#     def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
#         if not root:
#             return False
        
#         queue = [root, ]
#         cursum_queue = [0, ]
#         while queue:
#             # size = len(queue)
#             # for _ in range(size): 因为不涉及最短距离，所以可以不用这个for遍历一层的
#             node = queue.pop(0)
#             cursum = cursum_queue.pop(0)
#             cursum += node.val
#             if isLeaf(node):
#                 if cursum == targetSum:
#                     return True
#             if node.left:
#                 queue.append(node.left)
#                 cursum_queue.append(cursum)
#             if node.right:
#                 queue.append(node.right)
#                 cursum_queue.append(cursum)
#         return False

"""
Accepted
116/116 cases passed (52 ms)
Your runtime beats 63.63 % of python3 submissions
Your memory usage beats 5.48 % of python3 submissions (16.7 MB)
"""

def isLeaf(node):
    if not node.left and not node.right:
        return True
    else:
        return False

    
""" 深度递归法 """
# class Solution:
#     def hasPathSum(self, root, targetSum):
#         if not root:
#             return False
#         flag = False
#         def DFS(node, res):
#             nonlocal flag
#             if not flag:
#                 res = res + node.val
#                 if isLeaf(node) and res == targetSum:
#                     flag = True
#                 if node.left:
#                     DFS(node.left, res)
#                 if node.right:
#                     DFS(node.right, res)
#         DFS(root, 0)
#         return flag


""" 官方的深度递归 """
# class Solution:
#     def hasPathSum(self, root, targetSum):
#         if not root:
#             return False
#         if isLeaf(root):
#             return targetSum == root.val # 在当前层找到了目标
#         targetSum = targetSum - root.val # 将targetSum维护成下一层还需要找的数
#         return self.hasPathSum(root.left, targetSum) \
#                or self.hasPathSum(root.right, targetSum) 
#                # 在当前节点找下一层中满足条件的叶子节点
#                # return里递归or，则只需要找到一个True结果就为True



""" stack版迭代版深度优先 """
# class Solution:
#     def hasPathSum(self, root, targetSum):
#         if not root:
#             return False
#         stack = [(0, root), ]
#         while stack:
#             cursum, node = stack.pop() # （之前和，当前节点）
#             res = cursum + node.val # 加上当前节点的和
#             if isLeaf(node) and res == targetSum : # 是叶子节点且找到目标
#                 return True
#             else:
#                 if node.left:
#                     stack.append((res, node.left))
#                 if node.right:
#                     stack.append((res, node.right))

#             # 下面只对于全是正整数的成立，若存在负数，则不成立
#             # if res == targetSum: # 和等于目标
#             #     if not node.left and not node.right: # 当前节点为叶子节点
#             #         return True
#             # elif res < targetSum: # 把(当前和, 下一个节点)加入stack中，
#             #                       # 在下一轮pop出来看来就是(之前和，当前节点)
#             #     if node.left:
#             #         stack.append((res, node.left)) 
#             #     if node.right:
#             #         stack.append((res, node.right))
#             # else: # 当前和，超过了目标，进行剪枝
#             #     continue
#         return False
# """
# Accepted
# 116/116 cases passed (44 ms)
# Your runtime beats 93.88 % of python3 submissions
# Your memory usage beats 5.48 % of python3 submissions (16.7 MB)
# """


"""
本题要点：
迭代法：维护一个当前节点之前和状态，与当前节点同时进入容器内
递归法：将大问题转化为：当前节点的子节点是否为叶子节点和子节点=?目标-当前节点
"""

# 21-04-01 第二次做
class Solution:
    def hasPathSum(self, root, targetSum):

        def dfs(node, tar):
            if not node:
                return False
            lf, rt = False, False

            if not node.left and not node.right:
                return node.val == tar
            if node.left:
                lf = dfs(node.left, tar-node.val)
            if node.right:
                rt = dfs(node.right, tar-node.val)
            return lf or rt
        return dfs(root, targetSum)



# @lc code=end

