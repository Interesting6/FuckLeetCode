#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        size = len(secret)
        a, b = 0, 0
        from collections import defaultdict
        di = defaultdict(int)
        for c1, c2 in zip(secret, guess):
            if c1 == c2:
                a += 1
            else:
                if di[c2] > 0: # 可以消去
                    b += 1
                    di[c2] -= 1
                else: # 无法消去
                    di[c2] -= 1
                if di[c1] < 0: # 可以消去
                    b += 1
                    di[c1] += 1
                else: # 无法消去
                    di[c1] += 1
        
        res = f"{a}A{b}B"
        return res
"""
Accepted
152/152 cases passed (44 ms)
Your runtime beats 92.72 % of python3 submissions
Your memory usage beats 83.78 % of python3 submissions (14.8 MB)
"""
# secret = "1807"; guess = "7810"
# # secret = "1123"; guess = "0111"
# # secret = "1807";  guess = "7810"
# s = Solution().getHint(secret, guess)
# print(s)


# @lc code=end

