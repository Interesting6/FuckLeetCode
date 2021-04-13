# @before-stub-for-debug-begin
# from python3problem35 import *
# from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         def binarySearch(nums, target):
#             n = len(nums)
#             if n == 1:
#                 if target <= nums[0]:
#                     return 0
#                 else:
#                     return 1
#             mid = n // 2
#             if target <= nums[mid]: # 前部分搜索目标 
#                 return binarySearch(nums[:mid], target)
#             elif nums[mid] < target: # 在后半部分搜索目标，记得加上mid的坐标
#                 return mid + binarySearch(nums[mid:], target)

#         return binarySearch(nums, target)
# """
# Accepted
# 62/62 cases passed (32 ms)
# Your runtime beats 94.86 % of python3 submissions
# Your memory usage beats 15.27 % of python3 submissions (15.3 MB)
# """

# class Solution:
#     def searchInsert(self, nums, target):
#         n = len(nums)
#         def binarySearch(l, r): # 维护一个左闭右闭的区间
#             if l > r: # 区间不成立了
#                 return l
#             # 以下为l <= r的区间
#             m = (l+r) // 2
#             if nums[m] == target: # 找到了当前元素
#                 return m
#             elif target < nums[m]: # tartget在左区间
#                 return binarySearch(l, m-1) # 因为右闭，且在m的左边即左区间，所以m-1
#             else:
#                 return binarySearch(m+1, r) # 因为左闭，且在m的右边即右区间，所以m+1
#         return binarySearch(0, n-1)
            

# 21-04-07 第三次做，还是写烂了，写不来。。。
class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)
        def bi_search(l, r): # 左闭右闭[l, r]
            while l <= r: # 相等时[l, r]仍是一个区间；退出时肯定是r < l 了，且l=r+1
                mid = l + ((r-l)>>1)  # 防止溢出
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target: # mid及其左边都比tar小，直接看mid+1及其右边
                    l = mid + 1 # 下一个搜索区间[mid+1, r]
                elif nums[mid] > target: # mid及其右边都比tar大，直接看mid-1及其左边
                    r = mid - 1 # 下一个搜索区间[l, mid-1]
            return r + 1  # 为什么返回r+1呢？
            # 最终肯定都是在[num[l=r]]只剩一元素，此时mid=l=r
            # 3·tar更小时，右边界左移，r=m-1=l-1，而num[r=l-1]<tar，插入的位置得放在r=l-1后面，则为r+1=l；
            # 2·tar更大时，左边界右移，l=m+1=r+1，而num[l=r+1]>tar，插入的位置得放在当前l即可，而l=r+1；
            # 所以最终返回的都是r+1
        res = bi_search(0, n-1)
        return res
"""
 分别处理如下四种情况
1. 目标值在数组所有元素之前  [0, -1]
2. 目标值等于数组中某一个元素 == return middle;
3. 目标值插入数组中的位置 [left, right]，return  right + 1
4. 目标值在数组所有元素之后的情况 [left, right]， return right + 1

"""

class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)
        if nums[n-1] < target: # 在数组末尾，单独判断
            return n
        def bi_search(l, r): # 左闭右闭[l, r]
            while l < r: # 退出时肯定是r == l 
                mid = l + ((r-l)>>1)  # 防止溢出
                if nums[mid] < target: # mid及其左边都比tar小，直接看mid+1及其右边
                    l = mid + 1 # 下一个搜索区间[mid+1, r]
                else: # mid及其右边都大于等于tar
                    r = mid # 下一个搜索区间[l, mid]
            return l # 不用管是l还是r，因为l=r
        res = bi_search(0, n-1)
        return res
"""输出为数组不小于target的数的位置"""
# nums = [1,3,5,6]
# target = 6
# s = Solution().searchInsert(nums, target)
# print(s)
# @lc code=end

