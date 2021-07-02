# @before-stub-for-debug-begin
# from python3problem279 import *
# from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
# def BFS(cand, t):
#     step = 0
#     queue = cand.copy()
#     while queue:
#         size = len(queue)
#         step += 1
#         for _ in range(size):
#             x = queue.pop(0)  # 当前节点
#             for i in cand: # 下一步的节点
#                 res = x # 当前的累加值 # 一定要注意这个
#                 res = i + res # 加上下一代的值
#                 if res == t: # 如果当前累加值是目标
#                     return step + 1 # 返回当前步数+下一代的1步
#                 elif res < t: # 当前累加值小于目标则继续进队列
#                     queue.append(res)
#                 else: # 当前累加值大于目标，直接把该路pass掉，用新的i即换新路
#                     continue    

# class Solution:
#     def numSquares(self, n: int) -> int:
#         li = []
#         i = 1
#         while i*i < n:
#             li.append(i*i)
#             i += 1
#         if i*i == n:
#             return 1
#         li = li[::-1]
#         # print(n, li, i)
#         res = BFS(li, n)
#         # print(f"final == {res}")
#         return res

# 2021-06-11每日一题
# class Solution:
#     def numSquares(self, n):
#         dp = [ i for i in range(n+1) ] # i的结果初始化为i（最坏情况，由1组成）
#         for i in range(1, n+1):
#             for j in range(1, i): # 为什么从1小的开始？
#                 if i - j*j >= 0:
#                     dp[i] = min(dp[i], dp[i-j*j]+1) # i可以表示为j*j和i-j*j的和
#                 else:
#                     break
#         res = dp[n]
#         return res
# """
# Accepted
# 588/588 cases passed (5504 ms)
# Your runtime beats 14.78 % of python3 submissions
# Your memory usage beats 25.47 % of python3 submissions (15.3 MB)
# """

class Solution:
    def numSquares(self, n):
        # 广度优先搜索，找到的肯定是最小步数的
        queue = [n]
        visited = {n}
        step = 0
        while queue:
            step += 1
            size = len(queue)
            for _ in range(size): # 不能少了这步，相当于一个分层结构
                node = queue.pop(0)
                residuals = [node - i*i for i in range(1, int(node**0.5)+1)]
                for resi in residuals:
                    if resi == 0:
                        return step
                    else:
                        if resi not in visited: # 如果resi访问过，之前访问的肯定更小，所以跳过，只存储没访问过的到queue
                            queue.append(resi)
                            visited.add(resi)

        return -1
"""
Accepted
588/588 cases passed (324 ms)
Your runtime beats 79.74 % of python3 submissions
Your memory usage beats 13.55 % of python3 submissions (15.9 MB)
"""

n = 12
s = Solution().numSquares(n)
print(s)

# @lc code=end

