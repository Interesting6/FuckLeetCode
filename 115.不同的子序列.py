#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         dis = {} # 记录s中每个字符出现的位置
#         for i,c in enumerate(s):
#             if c not in dis:
#                 dis[c] = [i, ]
#             else:
#                 dis[c].append(i)

#         li = [] # 按t中字符顺序，构建每个字符在s中的索引
#         for i, c in enumerate(t):
#             if c not in dis:
#                 return 0
#             li.append(dis[c])
        
#         # 对li中每个列表选取一个元素进行组合，要求选出来的元素能够构成一个递增数列。
#         n = len(li)
#         res = []
#         pth = []
#         def backtracking(i):
#             if i == n:
#                 res.append(pth[:])
#                 return
#             for j in li[i]:
#                 if i != 0:
#                     if j > pth[-1]:
#                         pth.append(j)
#                         backtracking(i+1)
#                         pth.pop()
#                     else:
#                         continue
#                 else:
#                     pth.append(j)
#                     backtracking(i+1)
#                     pth.pop()
#         backtracking(0)
#         # print(res)
#         return len(res)
"""超时了！！"""


"""动态规划"""
class Solution:
    def numDistinct(self, s, t):
        ns = len(s)
        nt = len(t) 
        # 俩字符串首部添加虚拟""
        dp = [[0 for j in range(ns+1)] for i in range(nt+1)] 
        for j in range(ns+1): # 初始值
            dp[0][j] = 1  # s中的""与t中1后的每个字符都不匹配
        for i in range(1, nt+1):
            for j in range(1, ns+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                    # 1、不让s[i]参与匹配，也就是需要让s中[0,i-1]个字符去匹配t中的[0,j]字符;
                    # 2、让s[i]参与匹配，也就是让s中[0,i-1]个字符去匹配t中[0,j-1]个字符即可。
                else: # 当前s中的j字符与t中i字符不匹配
                    dp[i][j] = dp[i][j-1] # 等于s中j-1字符与t字符匹配的结果
                    # 相当于只能让s中[0,i-1]个字符去匹配t中的[0,j]字符;
        return dp[-1][-1]
"""
Accepted
62/62 cases passed (52 ms)
Your runtime beats 56.79 % of python3 submissions
Your memory usage beats 44.74 % of python3 submissions (15.2 MB)
"""

# @lc code=end

