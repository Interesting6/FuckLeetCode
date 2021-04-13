#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            if node.left and node.right:
                p = node.left # 左子树一定也是只有右节点的单链表
                while p.right: # 走到最右边
                    p = p.right
                p.right = node.right
                node.right = node.left
                node.left = None
            elif node.left and not node.right:
                node.right = node.left
                node.left = None
            elif not node.left and node.right:
                pass
        dfs(root)


# @lc code=end

