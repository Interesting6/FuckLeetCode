# @before-stub-for-debug-begin
from python3problem209 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_ = n + 1 # 最短子串的大小初始化为n+1
        k = 0 # 滑窗的开始
        sum_ = 0 # 滑窗[k, j]内元素和
        for j in range(n):
            sum_ +=  nums[j] # 进入滑窗内
            while sum_ >= target:     # 这点挺关键的，只有当子串和大于该target时，才进行缩小
                min_ = min(min_, j-k+1)
                sum_ -= nums[k] # 滑窗最前面的元素离开
                k += 1          # 对应开始坐标也减小
        if min_ > n: # 表明没找到和比target大的子串
            return 0
        # print(min_)
        return min_


# @lc code=end

