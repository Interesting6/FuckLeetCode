#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 21-04-12 不会 看答案的。
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = float("-inf")
        def dfs(node):
            if not node:
                return 0
            nonlocal res
            left = max(dfs(node.left), 0) # 若左边小于0，则不要左边
            right = max(dfs(node.right), 0) # 若右边小于0则不要右边
            cur = node.val + left + right # ^形状的路径的和
            res = max(cur, res) # 该^路径是否最大，最大就更新
            ret_val = node.val + max(left, right) # 返回该子树路径和时，只能返回最大的那条分支
            return ret_val
        dfs(root)
        return res


# @lc code=end

