#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
"""暴力记忆法：
对每个i，向左找其最大的，向右找其最大的，
最后i处的水高被定义为 左最大与右最大中更小的那个 - 本身高度
记忆优化：
    * 先提前查找好每个位置的左边最大值(从左向右找)和右边最大值(从右向左找)
    * 而如果临时查找i左边最大值(从i向左找)和i右边最大值(从i向右找)方向刚好相反，且耗时
时间复杂度O(N)，空间复杂度O(N)
"""
# class Solution:
#     def trap(self, height) -> int:
#         res = 0
#         n = len(height)
#         if n == 0:
#             return 0
#         lf_max = [0] * n # 第i个位置的值表示在i的左边最大的值
#         rt_max = [0] * n
#         # 初始化
#         lf_max[0] = height[0]
#         rt_max[-1] = height[-1]
#         # 从左向右找i左边最大的，因为lf_max[i]维护的是i左边的值，所以从左向右查找
#         for i in range(1, n):
#             lf_max[i] = max(lf_max[i-1], height[i])
#         # 从右向左找i右边最大的，因为rt_max[i]维护的是i右边的值，所以从右向左找
#         for i in range(n-2, -1, -1):
#             rt_max[i] = max(rt_max[i+1], height[i])
        
#         # 计算
#         for i in range(1, n-1): # 收尾可不用考虑，肯定为0
#             res += min(lf_max[i], rt_max[i]) - height[i]
#         return res

"""
Accepted
320/320 cases passed (44 ms)
Your runtime beats 80.56 % of python3 submissions
Your memory usage beats 87.94 % of python3 submissions (14.9 MB)
"""

"""双指针法"""
class Solution:
    def trap(self, height):
        n = len(height)
        if n < 3:
            return 0
        lf_max = height[0]
        rt_max = height[-1]
        lf = 1
        rt = n-2
        res = 0
        while lf <= rt:
            lf_max = max(lf_max, height[lf]) # [0-lf]中最大的高度
            rt_max = max(rt_max, height[rt]) # [rt-n]中最大的高度
            # res += min(lf_max[i], rt_max[i]) - height[i] 等价于下面
            if lf_max < rt_max:
                res += lf_max - height[lf]
                lf += 1
            else:
                res += rt_max - height[rt]
                rt -= 1
        return res

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# s = Solution().trap(height)
# print(s)
"""
Accepted
320/320 cases passed (32 ms)
Your runtime beats 99.36 % of python3 submissions
Your memory usage beats 96.36 % of python3 submissions (14.9 MB)
"""

"""还可以用递减栈来解决！！！
遇到比栈顶大的，则可以形成积水，弹出栈顶为低洼，新栈顶为左边界，该值为右边界。
直到栈顶比该值大，把该大的值作为左边界加入栈中。
"""

# @lc code=end

