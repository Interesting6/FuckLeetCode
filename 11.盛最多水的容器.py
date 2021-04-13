#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_vol = 0
        while i < j:
            cur_vol = (j-i) * min(height[i], height[j])
            max_vol = max(max_vol, cur_vol)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_vol

"""
Accepted
60/60 cases passed (312 ms)
Your runtime beats 5.86 % of python3 submissions
Your memory usage beats 7.94 % of python3 submissions (24.5 MB)
"""
# @lc code=end

