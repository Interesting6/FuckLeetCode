#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(length):
            cnt = Counter(strs[i]) # 注意下面取出01时，是字符，而不是整数，否者会得到0。
            for p in range(m, cnt['0']-1, -1):  # 能够放下strs[i]中的0
                for q in range(n, cnt['1']-1, -1): # 同时能够放下strs[i]中的1
                    # 最多p个0和q个1
                    dp[p][q] = max(dp[p][q], dp[p-cnt['0']][q-cnt['1']] + 1)

        res = dp[m][n]
        # print(dp)
        return res

# strs = ["10","0001","111001","1","0"]
# m = 5; n = 3
# s = Solution().findMaxForm(strs, m, n)
# print(s)
"""
Accepted
70/70 cases passed (4620 ms)
Your runtime beats 24.6 % of python3 submissions
Your memory usage beats 87.01 % of python3 submissions (15 MB)
"""
# @lc code=end

