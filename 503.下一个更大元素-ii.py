# @before-stub-for-debug-begin
from python3problem503 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        stack = []
        size = len(nums)
        li = [-1] * size
        for i,x in enumerate(nums):
            if not stack:
                stack.append((i, x))
            else:
                l = len(stack) - 1
                while l > -1:
                    if stack[l][1] < x:
                        li[stack[l][0]] = x
                        stack.pop()
                        l -= 1
                    else:
                        stack.append((i, x))
                        break
                if l == -1:
                    stack.append((i, x))
        if stack: # 最后剩余的元素构成单调递减栈
            idx = stack[0][0]
            for i,x in stack: # 对栈里每个元素
                for j in range(idx+1): # 比较前面这几个元素即可
                    if nums[j] > x:
                        li[i] = nums[j]
                        break
        return li

"""
Accepted
224/224 cases passed (216 ms)
Your runtime beats 91.23 % of python3 submissions
Your memory usage beats 8.61 % of python3 submissions (16.9 MB)
"""

##  官方题解  循环两次即可，更简便



# @lc code=end

