#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals):
        n = len(intervals)
        if n == 1:
            return intervals
        intervals.sort()
        res = [intervals[0]]
        for it in intervals[1:]:
            if it[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], it[1])
            else:
                res.append(it)
        # print(res)
        return res

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# # intervals = [[1,4],[4,5],[0, 8]]
# s = Solution().merge(intervals)
"""
Accepted
168/168 cases passed (40 ms)
Your runtime beats 95.3 % of python3 submissions
Your memory usage beats 30.44 % of python3 submissions (15.6 MB)
"""
# @lc code=end

