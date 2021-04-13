#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        p1 = 0
        p2 = n-1
        while p1 < p2 and nums[p1] == 0:
            p1 += 1
        while p1 < p2 and nums[p2] == 2:
            p2 -= 1
        if p1 >= p2:
            return
        i = p1
        while i <= p2:
            if nums[i] == 1: # n[i]==1时i才自增，当前的不动
                i += 1 
            elif nums[i] == 2: # 当前的换到后面
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            elif nums[i] == 0: # 当前的换到前面
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1 
            while p1 < p2 and nums[p2] == 2:
                p2 -= 1
            while p1 < p2 and nums[p1] == 0:
                p1 += 1   
            if i < p1: # i在p1左时，更新i到p1处
                i = p1
        # print(nums)

# nums = [2,0,2,1,1,0]
# nums = [0,0,2,1,0,1,2,0,1,2,0]
# nums = [2,0,1]
# s = Solution().sortColors(nums)
"""
Accepted 思路想起来比较简单，但实现起来有点困难
87/87 cases passed (36 ms)
Your runtime beats 83.55 % of python3 submissions
Your memory usage beats 15.32 % of python3 submissions (14.9 MB)
"""

# @lc code=end

