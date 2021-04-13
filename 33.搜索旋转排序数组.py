#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        for i in range(n-1):
            if nums[i] == target:
                return i
            if nums[i] > nums[i+1]:
                break
        if i == n-1:
            if nums[i] == target:
                return i
            else:
                return -1
        def bi_search(l, r):
            while l <= r:
                m = l +((r-l)>>1)
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m
            return -1
        res = bi_search(i+1, n-1)
        return res
"""
Accepted
195/195 cases passed (32 ms)
Your runtime beats 95.19 % of python3 submissions
Your memory usage beats 54.97 % of python3 submissions (15.1 MB)
"""
# @lc code=end

