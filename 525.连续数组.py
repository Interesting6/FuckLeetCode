#
# @lc app=leetcode.cn id=525 lang=python3
#
# [525] 连续数组
#

# @lc code=start
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        length = len(nums)
        preSum = 0
        di = {0: -1}
        """关键点：遇到1就+1，遇到0就-1"""
        maps = [-1, 1] # 0 -> -1,  1 -> +1
        res = 0
        for i in range(length):
            preSum += maps[nums[i]]
            if preSum in di: # 出现了则说明在di[preSum]后出现了相等个0和1，才会让前缀和保持了不变。
                res = max(res, i - di[preSum])
            else:
                di[preSum] = i
            
        return res

# nums = [1,1,0,1,0,1]
# nums = [0,1,0,1,1]
# s = Solution().findMaxLength(nums)
# print(s)
"""
Accepted
564/564 cases passed (204 ms)
Your runtime beats 99.68 % of python3 submissions
Your memory usage beats 41.88 % of python3 submissions (19.5 MB)
"""

# @lc code=end

