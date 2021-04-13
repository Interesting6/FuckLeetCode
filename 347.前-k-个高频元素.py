# @before-stub-for-debug-begin
from python3problem347 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        res = heapq.nlargest(k, cnt, key=cnt.get)
        return res
"""
Accepted
21/21 cases passed (56 ms)
Your runtime beats 39.48 % of python3 submissions
Your memory usage beats 78.26 % of python3 submissions (17.4 MB)
"""
# @lc code=end

