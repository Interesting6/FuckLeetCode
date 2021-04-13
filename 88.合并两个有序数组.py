#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
# class Solution:
    # def merge(self, nums1, m, nums2, n) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     t = nums1[:m]
    #     i = 0
    #     j = 0
    #     k = 0
    #     while i<m and j<n:
    #         if t[i] < nums2[j]:
    #             nums1[k] = t[i]
    #             i += 1
    #             k += 1
    #         else:
    #             nums1[k] = nums2[j]
    #             j += 1
    #             k += 1
    #     while i<m:
    #         nums1[k] = t[i]
    #         i += 1
    #         k += 1
    #     while j<n:
    #         nums1[k] = nums2[j]
    #         j += 1
    #         k += 1

# 法二，从后面开始插入，省去了空间复杂度！
class Solution:
    def merge(self, nums1, m, nums2, n):
        p = m + n - 1
        p1 = m-1
        p2 = n-1
        while p2 >= 0:
            while p1>=0 and nums2[p2] < nums1[p1]: # p1先走完
                nums1[p], nums1[p1] = nums1[p1], nums1[p] 
                # 注意这里是在同一数组上交换，不是单纯赋值，否者会影响后面的数
                p1 -= 1
                p -= 1
            nums1[p] = nums2[p2] # 因为在不同数组上，赋值即可，不会影响后面的数
            p2 -= 1
            p -= 1

# @lc code=end

