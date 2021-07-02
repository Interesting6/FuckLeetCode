#
# @lc app=leetcode.cn id=1442 lang=python3
#
# [1442] 形成两个异或相等数组的三元组数目
#

# @lc code=start
from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        S = [0] * (n + 1)
        from collections import Counter
        cnt, total = Counter(), Counter()
        res = 0
        for k in range(1, n+1):
            S[k] = S[k-1] ^ arr[k-1]
            if S[k] in cnt:
                res += cnt[S[k]] * (k-1) - total[S[k]] # S_{k-1 + 1}，所以这里是k-1
            cnt[S[k-1]] += 1        # 下标i出现的次数
            total[S[k-1]] += (k-1)  # 下标i之和
        return res

# arr = [2,3,1,6,7]
# arr = [7,11,12,9,5,2,7,17,22]
# s = Solution().countTriplets(arr)
# print(s)
"""
若下标 i=i1,i2,⋯,im时均满足 S_i=S_{k+1}，即有重复多个S_i相等，
如果在计算S_i时就计算结果，这时候会有重复
实际结果为：(k−i1)+(k−i2)+⋯+(k−im) = m⋅k − (i1 + i2 +⋯+ im)
即要获得下标i出现的次数m，和下标i之和

Accepted
47/47 cases passed (44 ms)
Your runtime beats 83.01 % of python3 submissions
Your memory usage beats 33.33 % of python3 submissions (14.9 MB)
"""

# @lc code=end

