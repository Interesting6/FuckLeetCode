# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start

"""暴力深度优先搜索，超时"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        res = float("inf")
        resli = []
        memo = {}
        length = len(nums)
        path = [0]
        def dfs(i, dep):
            nonlocal res #, resli
            if dep == m:
                path.append(length)
                # print(path)
                li = []
                for x in range(m):
                    if (path[x], path[x+1]) not in memo:
                        memo[(path[x], path[x+1])] = sum(nums[path[x]:path[x+1]])
                    li.append(memo[(path[x], path[x+1])])
                maxv = max(li)
                if maxv < res:
                    res = maxv
                    # li = []
                    # for x in range(m):
                    #     li.append(nums[path[x]: path[x+1]])
                    # resli = li[:]
                path.pop()
                return
            for j in range(i, length-(m-dep)):
                path.append(j+1) # [前j+1, 后j+1)即[前j+1, j]
                dfs(j+1, dep+1)
                path.pop()

        dfs(0, 1)
        # print(resli)
        return res



        
# @lc code=end

