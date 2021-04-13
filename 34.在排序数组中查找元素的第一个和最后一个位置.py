#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums, target: int):
        n = len(nums)
        if n == 0:
            return [-1, -1]
        def bi_search_left(l, r): # 缩小左边界，找左边第一个
            while l < r: # 最后一次肯定是[l, r=l+1]
                m = l + ((r-l)>>1) # 让m等于左边那个：m=l；若中间比tar小，则l=l+1；反之，r=l；最终都会让l=r
                if nums[m] < target:
                    l = m + 1  # 不能等于m，否者因为计算m时结果默认靠近左边，若进入这个循环即会进入死循环
                elif nums[m] >= target:
                    r = m
            if nums[l] == target:
                return l
            else:
                return -1, l
        def bi_search_right(l, r): # 缩小右边界
            while l < r: # 最后一次肯定是[l, r=l+1]
                m = l + ((r-l+1)>>1) # 让m等于右边那个：m=r；若中间比tar大，则r=r-1；反之l=r；最终都会让l=r
                if nums[m] > target: # 与上面的相反
                    r = m - 1
                elif nums[m] <= target:
                    l = m 
            if nums[r] == target:
                return r
            else:
                return -1, r
        lf = bi_search_left(0, n-1)
        rt = bi_search_right(0, n-1)
        return [lf, rt]

nums = [5,7,7,8,8,10]
# nums = []
target = 9
s = Solution().searchRange(nums, target)
print(s)

"""
Accepted
88/88 cases passed (36 ms)
Your runtime beats 89.04 % of python3 submissions
Your memory usage beats 60.71 % of python3 submissions (15.6 MB)
"""

# @lc code=end

