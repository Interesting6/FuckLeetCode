#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132模式
#

# @lc code=start
"""枚举j3，同时枚举k2，维护最小的i1，时间复杂度为O(N*N)"""
# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         n = len(nums)
#         inf = float("inf")
#         lf_min = nums[0]
#         for i in range(1, n):
#             if lf_min < nums[i]:
#                 for k in range(i+1, n):
#                     if lf_min < nums[k] < nums[i]:
#                         return True
#             elif lf_min > nums[i]:
#                 lf_min = nums[i]
#         return False


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        inf = float("inf")
        lf_min = [0]* n
        lf_min[0] = nums[0]
        for i in range(1, n):
            lf_min[i] = min(lf_min[i-1], nums[i])
        stack = [] # 总是维护在j之后且比当前j值小的k值，栈内递减
        for j in range(n-1, -1, -1):
            mxk = float("-inf")
            while stack and stack[-1] < nums[j]:
                mxk = stack.pop() # mk为2 < num[j]为3
            # 弹出的mxk必定是比n[j]小的最大值
            if lf_min[j] < mxk: # 栈内有比j3小的k2
                return True
            stack.append(nums[j]) # 否者栈内无比当前j更小的k值，把当前元加入
        return False

# @lc code=end

