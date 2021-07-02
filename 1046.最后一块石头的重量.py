#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
from heapq import heappop
from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        import heapq
        hp = [ -i for i in stones]
        heapq.heapify(hp)
        while len(hp) > 1:
            fst = - heapq.heappop(hp)
            scd = - heapq.heappop(hp)
            t = fst - scd
            if t > 0:
                heapq.heappush(hp, -t)
        if len(hp) == 1:
            res = -hp[0]
        else:
            res = 0
        return res

# stones = [2,7,4,1,8,1]
# s = Solution().lastStoneWeight(stones)
# print(s)
"""
Accepted
70/70 cases passed (32 ms)
Your runtime beats 96.65 % of python3 submissions
Your memory usage beats 14.37 % of python3 submissions (14.9 MB)
"""
# @lc code=end

