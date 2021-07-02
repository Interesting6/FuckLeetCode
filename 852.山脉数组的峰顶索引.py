#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)
        l, r = 0, length-1
        while l < r:
            m = l + ((r-l)>>1)
            if arr[m-1] < arr[m] and arr[m] > arr[m+1]:
                return m
            elif arr[m] < arr[m+1]:
                l = m + 1
            elif arr[m-1] > arr[m]:
                r = m #- 1 # 减不减一都无所谓的样子
        return l
"""
Accepted
34/34 cases passed (40 ms)
Your runtime beats 74.95 % of python3 submissions
Your memory usage beats 66.59 % of python3 submissions (15.7 MB)
"""

# arr = [0,1,0]
# arr = [0,2,1,0]
arr = [24,69,100,99,79,78,67,36,26,19]
# arr = [3,4,5,1]
s = Solution().peakIndexInMountainArray(arr)
print(s)

# @lc code=end

