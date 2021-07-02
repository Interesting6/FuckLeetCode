#
# @lc app=leetcode.cn id=1310 lang=python3
#
# [1310] 子数组异或查询
#

# @lc code=start
from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        all_ = 0
        lf = [0] * (n)
        rt = [0] * (n)
        for i in range(n):
            all_ ^= arr[i]
            if i < n-1:
                lf[i+1] = lf[i] ^ arr[i] # i前的值与当前i值得到i+1前的值
                j = n-1-i      # i从第一个开始到倒数第二个；j从最后一个开始到顺数第二个(不包括0)
                rt[j-1] = rt[j] ^ arr[j] # j-1后的 = j ^ j后的
        # print(lf, rt)
        res = []
        for l,r in queries:
            res.append(all_ ^ lf[l] ^ rt[r])
        return res

# arr = [1,3,4,8]
# queries = [[0,1],[1,2],[0,3],[3,3]]
# s = Solution().xorQueries(arr, queries)
# print(s)
"""
Accepted
42/42 cases passed (552 ms)
Your runtime beats 5.77 % of python3 submissions
Your memory usage beats 71.79 % of python3 submissions (29.1 MB)
"""

# @lc code=end

