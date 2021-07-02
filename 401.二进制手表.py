#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
from typing import List
# & 枚举法，小时和分钟分别枚举
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn >= 9:
            return []
        res = []
        template = "{h}:{m}"
        for h in range(0, 12):
            h1 = format(h, 'b').count('1')
            for m in range(0, 60):
                m1 = format(m, 'b').count('1')
                if (h1 + m1 == turnedOn):
                    t = str(m).zfill(2)
                    res.append(template.format(h=h, m=t))
        return res
""" # ! 这都居然99%
Accepted
10/10 cases passed (20 ms)
Your runtime beats 99.85 % of python3 submissions
Your memory usage beats 9.06 % of python3 submissions (15.1 MB)
"""

# s = Solution().readBinaryWatch(1)
# print(s)

# class Solution:
#     def readBinaryWatch(self, turnedOn: int) -> List[str]:
#         if turnedOn >= 9:
#             return []
#         res = []
#         nums = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
#         tmplate = "{h}:{m}"
#         def backtrack(pos: int, hset: set, mset: set):
#             if (pos == turnedOn):
#                 res.append()
#                 return


# @lc code=end

