#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        def memo(func):
            di = {}
            def wrapper(*args, **kwargs):
                if args in di:
                    return di[args]
                else:
                    res = func(*args, **kwargs)
                    di[args] = res
                    return res
            return wrapper
        @memo
        def f(n):
            if n==1 or n == 2 or n == 3 or n == 5:
                return True
            if n % 2 == 0:
                return f(n>>1)
            elif n % 3 == 0:
                return f(n//3)
            elif n % 5 == 0:
                return f(n//5)
            else:
                return False
        if n <= 0:
            return False
        res = f(n)
        return res
""" 写麻烦了，好像不会涉及到重复计算
Accepted
1013/1013 cases passed (40 ms)
Your runtime beats 75.91 % of python3 submissions
Your memory usage beats 90.21 % of python3 submissions (14.7 MB)
"""
# @lc code=end

