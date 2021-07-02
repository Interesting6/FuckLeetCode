#
# @lc app=leetcode.cn id=1449 lang=python3
#
# [1449] 数位成本和为目标值的最大数字
#

# 6.12日的dfs，超时
# @lru_cache(2048) # 还是超时通不过
# def dfs(t, s):
#     nonlocal ans
#     for c in cost: # 从小到大的
#         if t >= c[1]:
#             residual = t - c[1]
#             if residual == 0: # 找到一个解，
#                 ans = max(ans, s*10+c[0])
#             else: # 没有找到，继续找
#                 dfs(residual, s*10+c[0])
#         else: # 后面的都大于，不用进行
#             break
# dfs(target, 0)
# dfs.cache_clear()

### 三叶的
# dp = [float("-inf")] * (target + 1)
# dp[0] = 0
# for i in range(1, 10):
#     c = cost[i-1]
#     for j in range(c, target+1):
#         dp[j] = max(dp[j], dp[j-c]+1)
# if dp[target] < 0:
#     return "0"
# ans = ""
# j = target
# for i in range(9, 0, -1):
#     c = cost[i-1]
#     while j >= c and dp[j]==dp[j-c]+1: # j可由j-c和c拼出
#         ans += str(i)
#         j -= c
# return ans

# @lc code=start
from typing import List
from functools import lru_cache
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        cost = list(enumerate(cost, 1))
        cost.sort(key=lambda x: (x[1], -x[0]))
        print(cost)
        ans = 0
        dp = [""] * (target+1)
        for (i, v) in cost:
            for j in range(v, target+1):
                pass

        

cost = [4,3,2,5,6,7,2,5,5]; target = 9
# cost = [2,4,6,2,4,6,4,4,4]; target = 5
# cost = [6,10,15,40,40,40,40,40,40]; target = 47
s = Solution().largestNumber(cost, target)
print(s)

# @lc code=end

