#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, cur = [], root
        res = []
        pre = None # 上一个处理的节点
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not cur.right or cur.right == pre:
                # 处理节点
                res.append(cur.val)
                pre = cur
                cur = None
            else:
                stack.append(cur)
                cur = cur.right
        return res


# @lc code=end

