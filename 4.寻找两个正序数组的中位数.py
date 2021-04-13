#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) -> float:
#         m, n = len(nums1), len(nums2)
#         t = m + n
#         mid = t >> 1
#         p1 = 0
#         p2 = 0
#         pre = cur = 0
#         for k in range(mid+1): # 注意是到mid
#             pre = cur
#             if p1 < m and p2 < n:
#                 if nums1[p1] < nums2[p2]:
#                     cur = nums1[p1]
#                     p1 += 1
#                 else:
#                     cur = nums2[p2]
#                     p2 += 1
#             else: # 有一个没到顶，一个到顶了
#                 if p1 < m:
#                     cur = nums1[p1]
#                     p1 += 1
#                 if p2 < n:
#                     cur = nums2[p2]
#                     p2 += 1
#         if t & 1 == 0:
#             return (pre+cur) / 2
#         else:
#             return cur

""" 用pre来记录前一个，cur记录当前的值
Accepted，时间复杂度为O(m+n)
2094/2094 cases passed (48 ms)
Your runtime beats 85.57 % of python3 submissions
Your memory usage beats 17.69 % of python3 submissions (15.2 MB)
"""   


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        

            
# @lc code=end

