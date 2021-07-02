#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        q, r = divmod(num, 1000)
        res += q*'M'
        if r >= 900:
            res += "CM"
            r = r - 900
        q, r = divmod(r, 500)
        res += q*'D'
        if r >= 400:
            res += "CD"
            r = r - 400
        q, r = divmod(r, 100)
        res += q*"C"
        if r >= 90:
            res += "XC"
            r -= 90
        q, r = divmod(r, 50)
        res += q*"L"
        if r >= 40:
            res += "XL"
            r -= 40
        q, r = divmod(r, 10)
        res += q*"X"
        if r == 9:
            res += "IX"
            r -= 9
        q, r = divmod(r, 5)
        res += q*"V"
        if r == 4:
            res += "IV"
            r -= 4
        q, r = divmod(r, 1)
        res += q*"I"
        return res

# s = Solution().intToRoman(900)
# print(s)
"""
Accepted
3999/3999 cases passed (56 ms)
Your runtime beats 65.45 % of python3 submissions
Your memory usage beats 79.29 % of python3 submissions (14.8 MB)
"""
# @lc code=end

