#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        stack = []
        remain = False
        for i,it in enumerate(intervals):
            if it[1] < newInterval[0]: # 区间右边都小于插入区间的左边，直接加入
                stack.append(it)
            elif newInterval[1] < it[0]: # 区间左边比要插入的区间右边大，
                remain = True
                break # 跳出去把要插入的先插入，然后再把区间剩余的插入
            else: # 要插入的区间与当前区间有交集，将他们取并集到要插入的区间
                newInterval[0] = min(newInterval[0], it[0])
                newInterval[1] = max(newInterval[1], it[1])
        stack.append(newInterval)
        if remain:
            stack.extend(intervals[i:])
        return stack
"""
Accepted
156/156 cases passed (44 ms)
Your runtime beats 73.56 % of python3 submissions
Your memory usage beats 72.27 % of python3 submissions (16.3 MB)
"""

# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]
# intervals = [[1,3],[6,9]]; newInterval = [2,5]
# intervals = []; newInterval = [5,7]
# intervals = [[1,5]]; newInterval = [2,3]
# intervals = [[1,5]]; newInterval = [2,7]
# s = Solution().insert(intervals, newInterval)
# print(s)

# @lc code=end

