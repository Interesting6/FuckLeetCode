#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        # return list(set(range(1, n+1)) - set(nums)) # beat 99.77%
        aux = [1]*n
        for i,it in enumerate(nums):
            aux[it-1] &= 0 # 出现就置零
        res = []
        for i, it in enumerate(aux):
            if it:
                res.append(i+1)
        return res

"""
Accepted
33/33 cases passed (100 ms)
Your runtime beats 97.08 % of python3 submissions
Your memory usage beats 96.23 % of python3 submissions (20.6 MB)
"""

# @lc code=end

