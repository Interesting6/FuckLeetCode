#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
import numpy
# @lc code=start
def gcd(a, b):
    return a if (b == 0) else gcd(b, a%b)

from typing import List
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if (n <= 2):
            return n
        res = 0
        for i in range(n):
            if (res > n-i or res > n//2):
                break
            mp = defaultdict(int)
            for j in range(i+1, n):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                if (x==0):
                    y = 1
                elif (y==0):
                    x = 1
                else:
                    if (y<0): # 避免-1/2，1/-2这样的不等
                        x, y = -x, -y  # 统一将分子大于0，即只有1/-2这种
                    gcdxy = gcd(x, y)
                    x, y = x//gcdxy, y//gcdxy # 避免1/2, 2/4这样的不等
                mp[(x, y)] += 1  # (x, y)来表示y/x斜率
            maxn = 0
            for (_, v) in mp.items(): # 遍历每个斜率中相等斜率的点数
                maxn = max(maxn, v+1) # 加1是因为2斜率相等时有3个点
            res = max(res, maxn)
        return res
"""
Accepted
33/33 cases passed (60 ms)
Your runtime beats 69.83 % of python3 submissions
Your memory usage beats 39.66 % of python3 submissions (15 MB)
"""
# points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# s = Solution().maxPoints(points)
# print(s)   

# @lc code=end

