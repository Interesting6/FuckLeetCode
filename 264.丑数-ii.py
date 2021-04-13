#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        cnt = 0
        ugly_set = {1}
        import heapq
        hp = [1]
        while cnt < n:
            i = heapq.heappop(hp)
            cnt += 1
            if i*2 not in ugly_set:
                ugly_set.add(i*2)
                heapq.heappush(hp, i*2)
            if i*3 not in ugly_set:
                ugly_set.add(i*3)
                heapq.heappush(hp, i*3)
            if i*5 not in ugly_set:
                ugly_set.add(i*5)
                heapq.heappush(hp, i*5)
        return i
# s = Solution().nthUglyNumber(2)
# print(s)
""" 需要用最小堆来维持，不能i从1递增枚举，也不能i递增若i不在丑数集合就将i*235加入，还是会超时
Accepted
596/596 cases passed (188 ms)
Your runtime beats 35.42 % of python3 submissions
Your memory usage beats 56.15 % of python3 submissions (14.9 MB)
"""

# 动态规划：

class Solution:
    def nthUglyNumber(self, n):
        dp = [1] * (n+1)
        p2, p3, p5 = 1, 1, 1 # 三个指针
        for i in range(2, n+1):
            time2, time3, time5 = dp[p2]*2, dp[p3]*3, dp[p5]*5
            dp[i] = min(time2, time3, time5)
            if dp[i] == time2:
                p2 += 1
            if dp[i] == time3: # 注意是if，而不是elif，否者p3与p2重复时，只会移动一个指针，造成了dp中有重复
                p3 += 1
            if dp[i] == time5:
                p5 += 1
        # print(dp)
        return dp[n]

"""
Accepted
596/596 cases passed (144 ms)
Your runtime beats 74.56 % of python3 submissions
Your memory usage beats 81.83 % of python3 submissions (14.8 MB)
"""

# @lc code=end

