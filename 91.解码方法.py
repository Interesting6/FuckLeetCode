#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)  # 注意这里是n+1个
        if s[0] == '0':
            return 0
        dp[0] = 1  # 边界条件
        for i in range(1, n+1): # 
            if s[i-1] != '0': # i单独作为一个字符
                dp[i] += dp[i-1]
            if i > 1 and s[i-2] != '0' and int(s[i-2:i])<=26:
                # i-1与i组成一个字符
                dp[i] += dp[i-2]
        res = dp[n]
        return res

# s = "1123"
# s = Solution().numDecodings(s)
# print(s)
"""
Accepted
269/269 cases passed (48 ms)
Your runtime beats 21.34 % of python3 submissions
Your memory usage beats 71.12 % of python3 submissions (14.9 MB)
"""
# @lc code=end

