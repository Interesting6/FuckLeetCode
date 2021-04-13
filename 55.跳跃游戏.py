#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        step = 0 + nums[0] # 维护当前能够到达的最远距离
        for i in range(1, n):
            if i <= step:
                step = max(step, i+nums[i])
            else: # 超出了当前能够到达的最远距离，跳不出去
                return False
        return True
"""
Accepted
75/75 cases passed (52 ms)
Your runtime beats 52.76 % of python3 submissions
Your memory usage beats 79.28 % of python3 submissions (16 MB)
"""   
# @lc code=end

