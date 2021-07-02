#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        right = sum(weights)
        left = max(weights)
        while left < right:
            mid = left + ((right - left)>>1)
            need, cur = 1, 0
            # need 为需要运送的天数
            # cur 为当前这一天已经运送的包裹重量之和
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w

            if need <= D:
                right = mid
            else:
                left = mid + 1

        return left

        

# weights = [1,2,3,4,5,6,7,8,9,10]; D = 5
# s = Solution().shipWithinDays(weights, D)
# print(s)
# @lc code=end

