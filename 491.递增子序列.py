#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums):
        n = len(nums)
        res = []
        pth = []
        def dfs(d, start_idx):
            if d > 1:
                res.append(pth[:])
            cur_layer_used = set() # 本层使用过的元素
            for i in range(start_idx, n):
                if (d == 0 or nums[i] >= pth[-1]):  # 当d==0时，直接加入；或者d!=0时，要递增的加入
                    if nums[i] not in cur_layer_used: # 反之若在本层中使用过，则剪枝掉
                        cur_layer_used.add(nums[i])
                        pth.append(nums[i])
                        dfs(d+1, i+1)
                        pth.pop()

        dfs(0, 0)
        return res
# 不用担心如果不满足递增的时候，停止向后搜索了，但后面可能有满足条件的。
# 实际上在第一个调用的for里就考虑了以每个数字作为开头的结果
# nums = [4, 3, 2, 1]
# nums = [4, 7, 6, 7, 3, 3, 5]
# s = Solution().findSubsequences(nums)
# print(s)

""" 递归函数内使用set记录本层使用过的元素，用于剪枝，比在将pth加入res时判断有没有重复(5%左右)快多了
Accepted
58/58 cases passed (72 ms)
Your runtime beats 89.49 % of python3 submissions
Your memory usage beats 32.61 % of python3 submissions (20.8 MB)
"""
# @lc code=end

