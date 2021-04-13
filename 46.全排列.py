# @before-stub-for-debug-begin
from python3problem46 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
"""删除、增加，时间复杂度较高"""
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         li = []
#         def dfs(nums):
#             if not nums:
#                 res.append(li[:])
#                 return
#             for i, num in enumerate(nums):
#                 li.append(nums.pop(i))
#                 dfs(nums)
#                 nums.insert(i, li.pop())
#         dfs(nums)
#         return res

"""
Accepted 这居然能不超时，在i处的pop和insert其实都是O(n)复杂度
25/25 cases passed (40 ms)
Your runtime beats 76.78 % of python3 submissions
Your memory usage beats 15.42 % of python3 submissions (15.1 MB)
"""

"""引入布尔数组used，false表示该数还未被使用"""
class Solution:
    def permute(self, nums):
        res = []
        if not nums:
            return []
        n = len(nums)
        used = [False for _ in range(n)] # 以空间换时间
        path = []
        def dfs(used):
            if n == sum(used): # 全部被用了
                res.append(path[:])
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True # O(1)复杂度
                    path.append(nums[i])
                    dfs(used)
                    used[i] = False
                    path.pop()
        dfs(used)
        return res
""" 反而更慢了？这不科学。。。
Accepted
25/25 cases passed (52 ms)
Your runtime beats 13.23 % of python3 submissions
Your memory usage beats 5.12 % of python3 submissions (15.2 MB)
"""

# @lc code=end

