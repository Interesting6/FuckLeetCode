# @before-stub-for-debug-begin
from python3problem450 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def dfs(node): 
            if not node:
                return None
            if node.val == key:  # 找到了
                if node.left and node.right: # 1、有左子树和右子树
                    r = node.right 
                    l = node.left
                    while r.left: # 找到右子树最左边的节点
                        r = r.left
                    r.left = l  # 只需将l连接到r的最底层左子树的左边
                    return node.right # 返回更新后的右子树，替换当前节点
                if not node.left:  # 2、仅有右子树，返回右子树，替换当前节点，即删除当前节点右节点补位
                    return node.right
                if not node.right: # 3、仅有左子树，返回左子树，替换当前节点
                    return node.left
                # 4、最后当前节点为叶子节点，直接删除，返回None，这里其实被py隐含了
            if node.val > key:
                node.left = dfs(node.left)
            elif node.val < key:
                node.right = dfs(node.right)
            return node
        root = dfs(root)
        return root
"""
Accepted
91/91 cases passed (80 ms)
Your runtime beats 81.87 % of python3 submissions
Your memory usage beats 76.72 % of python3 submissions (18.8 MB)
"""
# @lc code=end

