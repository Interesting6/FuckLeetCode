#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 1:
            return True
        low, high = 0, int(c**0.5) # 注意这里取根号
        while low <= high:
            t = low**2 + high**2
            if t == c:
                return True
            elif t > c:
                high -= 1
            elif t < c:
                low += 1
        return False

# s = Solution().judgeSquareSum(2)
# print(s)
"""
Accepted
124/124 cases passed (360 ms)
Your runtime beats 46.43 % of python3 submissions
Your memory usage beats 80.04 % of python3 submissions (14.8 MB)
"""
# @lc code=end

