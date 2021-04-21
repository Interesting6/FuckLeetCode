#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        dp = [0] * (n+1) # dp[i]代表s[:i]即前i个(即0~i-1)字符能否被表示
        dp[0] = 1 # 边界条件，空字符串
        for i in range(1, n+1): # 可以s[0:i]分解为s[0:j]与s[j:i]
            for j in range(0, i): # s[0:j]已经计算过就是dp[j]
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = 1 # 可以被表示，跳出循环
                    break
        return bool(dp[n])
            
                

# @lc code=end

