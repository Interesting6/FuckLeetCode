#
# @lc app=leetcode.cn id=1720 lang=python3
#
# [1720] 解码异或后的数组
#

# @lc code=start
from typing import List
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in encoded:
            first ^= i
            res.append(first)
        return res

# encoded = [1,2,3]
# first = 1
# s = Solution().decode(encoded, first)
# print(s)

# @lc code=end

