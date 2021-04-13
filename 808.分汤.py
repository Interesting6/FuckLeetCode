#
# @lc app=leetcode.cn id=808 lang=python3
#
# [808] 分汤
#

# @lc code=start
class Solution:
    def soupServings(self, N: int) -> float:
        Q, R = divmod(N, 25)
        N = Q + (R>0) # R>0则多需要一步
        if N > 500: # 超过了该数极限后就都为1了
            return 1
        @cache
        def f(a, b):
            if a <= 0:
                if b > 0:
                    return 1
                elif b <= 0:
                    return 0.5
            elif a > 0:
                if b <= 0:
                    return 0
                else:
                    return 0.25*(f(a-4, b) + f(a-3, b-1) + f(a-2, b-2) + f(a-1, b-3))
        res = f(N, N)
        return res

# @lc code=end

