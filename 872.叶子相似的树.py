#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # stack1, cur1 = [], root1
        # stack2, cur2 = [], root2
        def get1leaf(node): # 后序遍历选出叶子节点的顺序
            stack, cur = [], node
            pre = None
            res = []
            while stack or cur:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                cur = stack.pop() # 弹出的一定不为空
                if cur.right and cur.right != pre:
                    stack.append(cur)
                    cur = cur.right
                elif cur.right and cur.right == pre:
                    pre = cur
                    cur = None
                else: # 右节点不存在，
                    if not cur.left: # 左节点也不存在，即为叶子节点
                        res.append(cur.val)
                    pre = cur
                    cur = cur.right # None
            return res
        res1 = get1leaf(root1)
        res2 = get1leaf(root2)
        # print(res1, res2)
        if len(res1) != len(res2):
            return False
        for i, j in zip(res1, res2):
            if i != j:
                return False
        return True
"""
Accepted
40/40 cases passed (52 ms)
Your runtime beats 15.01 % of python3 submissions
Your memory usage beats 46.27 % of python3 submissions (14.9 MB)
"""
        
# @lc code=end

