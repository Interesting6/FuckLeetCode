#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
# class Solution:
#     def subsets(self, nums):
#         n = len(nums)
#         res = []
#         li = []
#         pth = []
#         def f(d=0): # 得到各个元素选择与不选择的组合
#             if d == n:
#                 li.append(pth[:])
#                 return
#             for i in [0, 1]:
#                 pth.append(i)
#                 f(d+1)
#                 pth.pop()
#         f(0)
#         print(li)

# class Solution:
#     def subsets(self, nums):
#         n = len(nums)
#         li = []
#         pth = []
#         def f(d=0):
#             if d == n:
#                 li.append(pth[:])
#                 return
#             for i in [0, 1]:
#                 if i == 1: # 选择该元素
#                     pth.append(nums[d])
#                     f(d+1)  # 进入下一个元素是否选择
#                     pth.pop()
#                 else:     # 不选择该元素，进入下一个元素
#                     f(d+1)
#         f(0)
#         # print(li)
#         return li


"""回溯"""
class Solution:
    def subsets(self, nums):
        n = len(nums)
        res = []
        pth = []
        def f(d):
            res.append(pth[:]) # 直接加进去
            for i in range(d, n):
                pth.append(nums[i])
                f(i+1) # 这里是i+1表示num中的下一个位置开始选，这样13后不会再选2，只会选3之后的
                # 反之，若为d+1，表示i从当前层的[d, n]选，如[1, 3]，[2, 3], [3, 3]，3可以被选择3次
                pth.pop()
        f(0)
        return res


s = Solution().subsets([1,2,3])
print(s)

# @lc code=end

