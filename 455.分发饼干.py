# @before-stub-for-debug-begin
from python3problem455 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
"""
大饼干可满足大孩子和小孩子，
那么就应该优先满足胃口大的孩子，后面的小饼干可能满足小的孩子；
若优先满足小的孩子，后面的小饼干肯定不可能满足大孩子；
所以应该先用大饼干去满足大孩子。

小饼干虽然不能满足大孩子，但可能可以满足小孩子；
小孩子若不能被大饼干满足，那肯定也不能被小饼干满足。
所以应该对每个孩子进行遍历！！！
"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        satisfied = 0
        i = 0
        j = 0
        ng = len(g)
        ns = len(s)
        g.sort(reverse=True)
        s.sort(reverse=True)
        cake_idx = 0
        for p in g:
            if cake_idx < ns: # 有饼干
                if s[cake_idx] >= p:
                    satisfied += 1
                    cake_idx += 1 # 饼干向后移一位
                # else 后面所有饼干都满足不了该孩子
                # 跳到下一个孩子，且饼干的索引不变
            else: # 无饼干了，直接退出
                break
        # """以下不成立"""
        # peop_idx = 0
        # for c in s: """用每块饼干去满足胃口大的大孩子是不可行的！！！"""
        #     if peop_idx < ng: # 有人
        #         if c >= g[peop_idx]: 
        #             satisfied += 1
        #             peop_idx += 1
        #         # else 该饼干虽然不能满足该大孩子，但可以满足后面的小孩子
        #     else:
        #         break
        return satisfied
"""
Accepted
21/21 cases passed (48 ms)
Your runtime beats 99.5 % of python3 submissions
Your memory usage beats 16.65 % of python3 submissions (16 MB)
"""
# class Solution:
#     # 这种方法虽然可行，但速度还是挺慢，因为每次都重头开始遍历了饼干。
#     def findContentChildren(self, g, s):
#         g.sort(reverse=True)
#         s.sort(reverse=True)
#         ns = len(s)
#         satisfied = 0
#         for p in g:
#             for i in range(ns):
#                 if s[i] and s[i] >= p:
#                     satisfied += 1
#                     s[i] = 0
#                     break
#                 break # 当前饼干都不满足，后面的肯定也不满足
#         return satisfied
        

# @lc code=end

