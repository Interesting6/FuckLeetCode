#
# @lc app=leetcode.cn id=1074 lang=python3
#
# [1074] 元素和为目标值的子矩阵数量
#

# @lc code=start
# from typing import List
# class Solution:
#     def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
#         m, n = len(matrix), len(matrix[0])
#         preSum = [[0]*(n+1) for _ in range(m+1)]
#         for i in range(m):
#             for j in range(n):
#                 preSum[i+1][j+1] = preSum[i+1][j] + preSum[i][j+1] - preSum[i][j] + matrix[i][j]

#         ans = 0
#         # 暴力求解
#         for i in range(1, m+1):
#             for j in range(1, n+1):  # 左上
#                 for p in range(i, m+1): 
#                     for q in range(j, n+1): # 右下
#                         if preSum[p][q] - preSum[p][j-1] - preSum[i-1][q] + preSum[i-1][j-1] == target:
#                             ans += 1
#                         # 画个图就明了了，左上的i,j是要减一的。否者会吧自己减去自己算进去。
#         """python超时，看答案说其他的语言不一定超时"""
#         return ans        

"""hash表优化"""
from typing import List
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        preSum = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                preSum[i+1][j+1] = preSum[i+1][j] + preSum[i][j+1] - preSum[i][j] + matrix[i][j]

        ans = 0
        for top in range(1, m+1): # 上边界
            for bot in range(top, m+1):  # 下边界
                di = {} # 固定了上下界，变成了一个一维搜索
                for rt in range(0, n+1): # 遍历右边界，在hash表中找左边界了；从0开始代表不需要单独考虑 最左到rt的值的情况，即下面cur==target的情况
                    cur = preSum[bot][rt] - preSum[top-1][rt]
                    # if cur == target: # 从最左边到rt位置的子矩阵，即左上[top, 0] -> 右下[bot, rt]
                    #     ans += 1      # 注意这种写法时，rt是从1开始，表示从最左到rt单独考虑，而从0开始的话已经考虑了最左的情况
                    if cur - target in di: # 在rt的左边lf处，存在[0:lf]的一维前缀和值为cur-tartget
                        # 这样[lf:rt]的和就为cur - (cur-target) = target
                        ans += di[cur - target]  # 有几个lf都满足
                    di[cur] = di.get(cur, 0) + 1 # 维护左边界lf的一维前缀和[0:lf]为cur的个数
                    
        return ans   


# matrix = [[0,1,0],[1,1,1],[0,1,0]]; target = 0
# s = Solution().numSubmatrixSumTarget(matrix, target)
# print(s)
"""
Accepted
40/40 cases passed (576 ms)
Your runtime beats 98.36 % of python3 submissions 
Your memory usage beats 85.25 % of python3 submissions (15.3 MB)
"""

# @lc code=end

