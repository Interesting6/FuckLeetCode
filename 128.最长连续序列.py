#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        di = {} # key存放连通区域的数，value为该数对应的连通区域长度
        res = 0
        for i in nums:
            if i not in di: # 当前数不在di里，避免了重复，
                # i-1和i+1只可能出现在边界，而不会出现在一个连通区域里，
                # 所以最后只需要更新连通区域的边界值对应该连通区域的长度
                lf_len = di.get(i-1, 0) # i-1所在连通区域的大小，若未出现过，则为0
                rt_len = di.get(i+1, 0) # i+1所在连通区域的大小
                cur_len = lf_len + 1 + rt_len
                res = max(res, cur_len)
                # 这时i把i前面的连通区域和i后面的连通区域连接了起来，变成了一个大的连通区域
                di[i] = cur_len
                di[i-lf_len] = cur_len # 更新该连通区域的左边界对应的连通区域的长度
                di[i+rt_len] = cur_len # 该连通区域的右边界

        # print(di)
        return res

# nums = [0,3,7,2,5,8,4,6,0,1, 11]
# nums = [100,4,200,1,3,2]
# s = Solution().longestConsecutive(nums)
# print(s)
"""
Accepted
70/70 cases passed (116 ms)
Your runtime beats 15.7 % of python3 submissions
Your memory usage beats 5.01 % of python3 submissions (27.7 MB)
"""
# @lc code=end

