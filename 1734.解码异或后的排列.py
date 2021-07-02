#
# @lc app=leetcode.cn id=1734 lang=python3
#
# [1734] 解码异或后的排列
#

# @lc code=start
from typing import List
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        res = [0] * (n)
        res1 = 0
        for i in range(1, n+1):
            res1 ^= i
        res2 = 0
        for i in range(n):
            if i % 2 == 1:
                res2 ^= encoded[i]
        res[0] = res1 ^ res2
        for i in range(1, n):
            res[i] = encoded[i-1] ^ res[i-1]
        # print(res)
        return res

"""
Accepted
63/63 cases passed (284 ms)
Your runtime beats 17.07 % of python3 submissions
Your memory usage beats 81.71 % of python3 submissions (29.7 MB)
"""

# @lc code=end

