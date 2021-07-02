# @before-stub-for-debug-begin
from python3problem437 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start #& 关键是要通过路径方向必须向下这点想到前缀和
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 21-06-26  不会
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        ans = 0
        di = dict() # 存前缀和->该前缀和对应的节点数量，（重复路径）
        def dfs(node, curSum):
            if not node:
                return 0
            res = 0
            curSum += node.val 
            res += di.get(curSum - targetSum, 0) #&1 是否存在preSum + target = curSum 是则满足的个数
            di[curSum] = di.get(curSum, 0) + 1  #&2 更新当前树的前缀和

            lf = dfs(node.left, curSum) 
            rt = dfs(node.right, curSum)
            res = res + lf + rt  # 到当前路径的结果 + 左子结果 + 右子结果
            di[curSum] = di[curSum] - 1 # 状态恢复？#&3 防止左树的前缀和影响右树前缀和的结果，对应&2。
            return res
        di[0] = 1  # 前缀和为0时，初始化为1？
        ans = dfs(root, 0)
        return ans


# @lc code=end

