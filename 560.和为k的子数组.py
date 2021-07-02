#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)

        ans = 0
        preSum = [0] * length
        di = {}
        di[k] = 1 # 初始化，若找到则表示从0开始到该位置
        for i, n in enumerate(nums):
            if i == 0 :
                preSum[i] = n
            else:
                preSum[i] = preSum[i-1] + n
            ans += di.get(preSum[i], 0) # 找到了
            di[preSum[i] + k] = di.get(preSum[i]+k, 0) + 1 # 更新di
        
        return ans

# nums = [1, 1, 1]; k = 2
# nums = [1, 2, 3, -3, -2, 2]; k = 3
# nums = [1,2,1,2,1]; k = 3
# nums = [3,4,7,2,-3,1,4,2]; k=7
# nums = [1]; k=0
# s = Solution().subarraySum(nums, k)
# print(s)

#### 遇到这种连续序列和的，一定要想到前缀和！
"""
Accepted
89/89 cases passed (116 ms)
Your runtime beats 17.95 % of python3 submissions
Your memory usage beats 12.89 % of python3 submissions (17.6 MB)
"""
# @lc code=end

