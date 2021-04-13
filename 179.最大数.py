#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if set(nums) == {0}:
            return '0'
        def sort_key(a, b): # a < b ? a在前b在后；否者b在前a在后
            p1 = a * 10**(len(str(b))) + b # a在前b在后
            p2 = b * 10**(len(str(a))) + a
            if p1 < p2: # 正序
                return -1
            elif p1 > p2: # 逆序
                return 1
            else:
                return 0 
        from functools import cmp_to_key
        nums.sort(key=cmp_to_key(sort_key), reverse=True)
        # 原本key函数是将列表里的每个元素转换为待比较的key，在key上进行比较
        # 而这里传入的是比较函数，所以需要用cmp_to_key对比较函数进行一个转化
        res = ''.join([str(i) for i in nums])
        return res
        

# nums = [3,30,34,345,5,9]
# s = Solution().largestNumber(nums)

# @lc code=end

