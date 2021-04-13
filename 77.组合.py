# @before-stub-for-debug-begin
from python3problem77 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        li = []
        # used = [0 for _ in range(n)]
        def dfs(depth, start_idx): # start_idx来控制每次搜索时候的起始位置
            if depth == k:
                res.append(li[:])
                return
            if n+1-start_idx + depth+1 < k: # 剪枝，
                return # 或者将下面range里的n+1减小到n+1- (k-(depth+1))好像会更好，可以省去进入空递归栈
            for i in range(start_idx, n+1): # 这里start_idx作为递归参数很关键
                li.append(i)
                dfs(depth+1, i+1)
                li.pop()
        dfs(0, 1)
        return res

"""
Accepted
27/27 cases passed (440 ms)
Your runtime beats 38.37 % of python3 submissions
Your memory usage beats 65.71 % of python3 submissions (16.1 MB)
"""


"""对一个数组内的元素进行组合的模板"""
# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         nums = [2, 4, 8, 13, 43]
#         k = 3
#         n = len(nums)
#         res = []
#         li = []
#         # used = [0 for _ in range(n)]
#         def dfs(depth, start_idx): # start_idx来控制每次搜索时候的起始位置
#             if depth == k:
#                 res.append(li[:])
#                 return
#             for i in range(start_idx, n): # 这里start_idx作为递归参数很关键，相当于该递归里用的元素是nums[start_idx:]
#                 li.append(nums[i]) # 将数组里对应元素加进去
#                 dfs(depth+1, i+1)
#                 li.pop()
#         dfs(0, 0) # 注意这里是从0开始
#         return res
# @lc code=end

