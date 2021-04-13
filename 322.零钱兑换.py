# @before-stub-for-debug-begin
from python3problem322 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         @cache
#         def dfs(x):
#             if x < 0:
#                 return -1
#             if x == 0:
#                 return 0
#             res = float("inf")
#             for c in coins:
#                 t = dfs(x-c)
#                 if t >= 0: # -1的不用计入
#                     res = min(res, t)
#             if res > 10**4:
#                 return -1
#             return res + 1 # f(x) = min_c_(f(x-c)) + 1
#         res = dfs(amount)
#         return res
"""
Accepted
182/182 cases passed (1324 ms)
Your runtime beats 54.87 % of python3 submissions
Your memory usage beats 14.51 % of python3 submissions (35.5 MB)
"""

# 21-04-02 第二次做
"""
状态：目标金额 x=amount
选择：数组中列出所有硬币面额 coins
函数的定义：凑出总金额x，至少需要f(x)枚硬币
base case: x<0 不可能凑出；x=0时，需要0枚硬币凑出
"""
class Solution:
    def coinChange(self, coins, amount):
        @cache
        def dfs(x):
            if x < 0: # 不可能凑出
                return -1
            if x == 0: # 凑出只需要1枚
                return 0
            res = float("inf")
            # 分解为子问题
            for c in coins:
                t = dfs(x-c) # 计算子问题的结果
                if t == -1: # 子问题无解，跳过
                    continue
                res = min(res, t+1)
            if res > 10**4:
                return -1
            return res
            
        res = dfs(amount)
        return res

# 自底向上
class Solution:
    def coinChange(self, coins, amount):
        dp = [amount+1] * (amount+1)
        dp[0] = 0 # base case
        # 外循环遍历状态的所有取值
        for i in range(1, amount+1):
            # 内循环遍历所有选择的最小值
            for c in coins:
                if i - c < 0:
                    continue
                dp[i] = min(dp[i], dp[i-c]+1)
        if dp[amount] == amount+1:
            return -1
        else:
            return dp[amount]


# @lc code=end

