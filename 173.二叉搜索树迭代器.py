#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 直接遍历存起来
# class BSTIterator:
#     def __init__(self, root: TreeNode):
#         from collections import deque
#         self.root = root
#         self.stack = []
#         self.res = deque([])
#         self.travel(root)

#     def travel(self, node):
#         while self.stack or node:
#             while node:
#                 self.stack.append(node)
#                 node = node.left
#             node = self.stack.pop()
#             self.res.append(node.val)
#             node = node.right

#     def next(self) -> int:
#         if self.hasNext():
#             return self.res.popleft()

#     def hasNext(self) -> bool:
#         return len(self.res) != 0

"""
Accepted
61/61 cases passed (84 ms)
Your runtime beats 85.83 % of python3 submissions
Your memory usage beats 10.74 % of python3 submissions (21.8 MB)
"""


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root = root
        self.stack = []
        self.travel(root)

    def travel(self, node):
        # 左边一路到底
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        if self.hasNext():
            node = self.stack.pop()
            if node.right:
                self.travel(node.right)
            return node.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0

"""
Accepted
61/61 cases passed (88 ms)
Your runtime beats 72.34 % of python3 submissions
Your memory usage beats 5.03 % of python3 submissions (21.9 MB)
"""

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

