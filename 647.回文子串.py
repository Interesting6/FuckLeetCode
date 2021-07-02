#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
# 21-06-24 看答案，未提交
class Solution:
    def countSubstrings2(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        def extend(l, r):
            #& 从[l, r]向两端扩展回文串
            res = 0
            while (0<=l and r<n and s[l]==s[r]):
                res += 1
                l -= 1
                r += 1
            return res
        res = 0
        for i in range(n):
            res += extend(i, i) #& 以i为中心
            res += extend(i, i+1) #& 以i和i+1为中心
        return res
    
    def countSubstrings(self, s):
        n = len(s)
        if n <= 1:
            return n
        dp = [[0]*n for _ in range(n)]
        res = 0
        for i in range(n-1, -1, -1): # 从下到上
            for j in range(i, n):    # 从左到右
                if (i==j):
                    dp[i][j] = 1
                elif (j==i+1 and s[i]==s[j]):
                    dp[i][j] = 1
                elif (s[i]==s[j] and dp[i+1][j-1]): # dp依赖于下左方元素
                    dp[i][j] = 1
                res += dp[i][j]
        return res

        
s = "abc"
sl = Solution().countSubstrings(s)
print(sl)

# @lc code=end

