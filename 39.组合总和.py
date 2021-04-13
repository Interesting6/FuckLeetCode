# @before-stub-for-debug-begin
from python3problem39 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        pth = []
        sum_ = 0
        n = len(candidates)
        candidates.sort()
        def backtracking(sum_, start_idx):
            if sum_ == target:
                res.append(pth[:])
                return
            elif sum_ > target:
                return
            # for num in candidates:
            for i in range(start_idx, n):
                sum_ += candidates[i]
                if sum_ > target: # 排序后的剪枝
                    sum_ -= candidates[i]
                    break
                pth.append(candidates[i])
                backtracking(sum_, i) 
                # 若为i+1，则是下层不能重复已经选择过的数字；
                # 而为i，即表示下层还可以重复用当前选择的数；但在横向for里，却能自动去除之前已选的。
                pth.pop()
                sum_ -= candidates[i]
        backtracking(sum_, 0)
        return res
"""
Accepted
170/170 cases passed (60 ms)
Your runtime beats 72.58 % of python3 submissions
Your memory usage beats 27.72 % of python3 submissions (15 MB)
"""

# @lc code=end

