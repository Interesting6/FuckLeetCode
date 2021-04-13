# @before-stub-for-debug-begin
from python3problem279 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#

# @lc code=start
def BFS(cand, t):
    step = 0
    queue = cand.copy()
    while queue:
        size = len(queue)
        step += 1
        for _ in range(size):
            x = queue.pop(0)  # 当前节点
            for i in cand: # 下一步的节点
                res = x # 当前的累加值 # 一定要注意这个
                res = i + res # 加上下一代的值
                if res == t: # 如果当前累加值是目标
                    return step + 1 # 返回当前步数+下一代的1步
                elif res < t: # 当前累加值小于目标则继续进队列
                    queue.append(res)
                else: # 当前累加值大于目标，直接把该路pass掉，用新的i即换新路
                    continue
        

class Solution:
    def numSquares(self, n: int) -> int:
        li = []
        i = 1
        while i*i < n:
            li.append(i*i)
            i += 1
        if i*i == n:
            return 1
        li = li[::-1]
        # print(n, li, i)
        res = BFS(li, n)
        # print(f"final == {res}")
        return res


# @lc code=end

