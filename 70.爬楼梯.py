#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        if n <= 1:
            return 1
        while n > 1:
            res = a + b
            a = b
            b = res
            n -= 1
        return res

# s = Solution().climbStairs(4)
# print(s)
# @lc code=end

