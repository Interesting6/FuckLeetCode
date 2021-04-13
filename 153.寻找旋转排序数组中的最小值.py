#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
# class Solution:
#     def findMin(self, nums) -> int:
#         return min(nums)
"""
在最小值右侧的值(不包括最后一个)肯定都严格小于num[r]，在最小值左边的肯定都严格大于num[r]；
根据这条性质找出最小值
"""
class Solution:
    def findMin(self, nums):
        n = len(nums)
        def bi_search(l, r):
            while l < r:
                m = l + ((r-l)>>1)
                if nums[m] < nums[r]: #比右侧小的m肯定在最小值右边，可以缩小r
                    r = m  # nums[m]可能是最小值
                else:
                    l = m + 1 # m肯定不是最小值，因为num[m]>=nums[r]，即num[m]的下界要比最小值大
            return nums[l]
        res = bi_search(0, n-1)
        return res
"""
Accepted
150/150 cases passed (24 ms)
Your runtime beats 99.76 % of python3 submissions
Your memory usage beats 11.51 % of python3 submissions (15.2 MB)
"""            

# @lc code=end

