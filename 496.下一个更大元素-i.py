#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         stack = []
#         nums2_next = [-1] * len(nums2)
#         for i, n in enumerate(nums2):
#             while stack:
#                 if stack[-1][1] < n:
#                     pre_i, pre_n = stack.pop()
#                     nums2_next[pre_i] = n
#                 else:
#                     break
#             stack.append((i, n))
#         res = []
#         for i, n in enumerate(nums1):
#             res.append(nums2_next[nums2.index(n)])
#         return res

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nums2_next = {}
        for n in nums2:
            while stack:
                if stack[-1] < n:
                    pre_n = stack.pop()
                    nums2_next[pre_n] = n
                else:
                    break
            stack.append(n)
        while stack:
            n = stack.pop()
            nums2_next[n] = -1
        res = []
        for i, n in enumerate(nums1):
            res.append(nums2_next[n])
        return res
"""
Accepted
15/15 cases passed (52 ms)
Your runtime beats 53.21 % of python3 submissions
Your memory usage beats 75.96 % of python3 submissions (15 MB) # 居然更耗内存？
"""
# @lc code=end

