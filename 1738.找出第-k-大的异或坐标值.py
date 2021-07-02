#
# @lc app=leetcode.cn id=1738 lang=python3
#
# [1738] 找出第 K 大的异或坐标值
#

# @lc code=start
from typing import List
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        preSum = [[0]*(n+1) for _ in range(m+1)]
        import heapq
        hp = []
        for i in range(1, m+1):
            for j in range(1, n+1):
                preSum[i][j] = preSum[i-1][j-1] ^ preSum[i][j-1] \
                    ^ preSum[i-1][j] ^ matrix[i-1][j-1]
                if len(hp) < k:
                    heapq.heappush(hp, preSum[i][j])
                else:
                    if preSum[i][j] > hp[0]:
                        heapq.heappop(hp)
                        heapq.heappush(hp, preSum[i][j])
                    else:
                        pass
        # print(hp)
        return hp[0]

# matrix = [[5,2],[1,6]]
# k = 4
# s = Solution().kthLargestValue(matrix, k)
# print(s)
"""
Accepted
49/49 cases passed (1464 ms)
Your runtime beats 52.17 % of python3 submissions
Your memory usage beats 81.16 % of python3 submissions (34.1 MB)
"""

# @lc code=end

