# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#

# @lc code=start
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        length = len(nums)
        if length == 1: # 暴力超时
            return False
        elif length == 2:
            return sum(nums) % k == 0
        
        preSum = [0] * (length+1)
        di = {}
        di[0] = -1
        for i in range(length):
            preSum[i+1] = preSum[i] + nums[i]
            t = preSum[i+1] % k
            if t in di:
                if(i - di[t]) > 1:
                    return True
                else: # 否者会一直更新di[t]，这样可能会保持i-di[t]总是为1，如[5,0,0,0]3的情况
                    continue
            else:
                di[t] = i
    
        return False

"""
Accepted
94/94 cases passed (124 ms)
Your runtime beats 28.18 % of python3 submissions
Your memory usage beats 49.81 % of python3 submissions (32.9 MB)
"""

# @lc code=end

