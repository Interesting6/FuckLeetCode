#
# @lc app=leetcode.cn id=1744 lang=python3
#
# [1744] 你能在你最喜欢的那天吃到你最喜欢的糖果吗？
#

# @lc code=start
from typing import List
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        preSum = [0] * (len(candiesCount) + 1)
        for i, c in enumerate(candiesCount):
            preSum[i+1] = preSum[i] + c
        answer = list()
        for i, (favTp, favDy, dlyCap) in enumerate(queries):
            minEat = favDy+1 # 最小糖果数
            maxEat = (favDy+1) * dlyCap # favDy这天能吃到的最大糖果数
            shouldhaveSum = preSum[favTp]
            nowSum = preSum[favTp+1]
            res = True
            if maxEat <= shouldhaveSum: # 每天都吃最大的容量，都吃不掉favTp前的糖果。
                res = False
            elif minEat > nowSum: # 每天吃最少的容量，但其实favTp已经被之前的天吃掉了。
                res = False
            answer.append(res)
        return answer

# candiesCount = [7,4,5,3,8]; queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
# candiesCount = [5,2,6,4,1]; queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
# s = Solution().canEat(candiesCount, queries)
# print(s)

# @lc code=end

