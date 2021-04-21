#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
# 超时了
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites) -> bool:
#         if not prerequisites:
#             return True
#         from collections import defaultdict
#         graph = defaultdict(list)
#         map_ = {}
#         for a,b in prerequisites:
#             graph[a].append(b) # a需要的先修课b，b->a有条边(b得先修)
#         searched = [0] * numCourses
#         res = []
#         ans = True
#         def dfs(node, pth):
#             nonlocal ans
#             if node in pth: # 在访问的路径上，意味着成环了
#                 ans = False
#                 return
#             searched[node] = 1 # 标记为访问过
#             pth.append(node)
#             if not graph[node]: # node无先修课了
#                 res.append(node)
#             for neib in graph[node]:
#                 dfs(neib, pth)
#                 if ans == False:
#                     return
#             pth.pop()

#         for i in range(numCourses):
#             if ans and searched[i] == 0:
#                 dfs(i, [])
#             else:
#                 pass
#         # print(res)
#         return ans
            


# 深度优先搜索
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        if not prerequisites:
            return True
        from collections import defaultdict
        graph = defaultdict(list)
        map_ = {}
        for a,b in prerequisites:
            graph[a].append(b) # a需要的先修课b，b->a有条边(b得先修)
            # 官方解答是b append a诶，其他人也是这样写，但这样我也通过了
        searched = [0] * numCourses
        res = []
        ans = True
        def dfs(node):
            nonlocal ans
            searched[node] = 1 # 标记为1，其中所有的1表示当前递归的node路径
            for neib in graph[node]:
                if searched[neib] == 0: # 未被访问过
                    dfs(neib)
                    if ans == False: # 已经找到环了，退出
                        return
                elif searched[neib] == 1: # 在递归的路径上
                    ans = False  # 回到了递归的路径上，成环了
                    return
                elif searched[neib] == 2: # 仅仅是访问过
                    pass
            searched[node] = 2 # 上面循环结束，代表以node递归深入的路径结束，将其从1设为2，表示访问过，且离开了递归的路径！妙啊！
            # res.append(node) # node无先修课了(未进行for)，或者其选修课已经修了(for已结束)！

        for i in range(numCourses):
            if ans and searched[i] == 0:
                dfs(i)
            else:
                pass
        # print(res)
        return ans
"""
Accepted
49/49 cases passed (52 ms)
Your runtime beats 53.95 % of python3 submissions
Your memory usage beats 32.63 % of python3 submissions (17.3 MB)
"""
# 广度优先搜索
class Solution:
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict, deque
        edge = defaultdict(list)
        in_deg = [0] * numCourses
        for a, b in prerequisites: # b -> a a需要b
            edge[b].append(a)
            in_deg[a] += 1

        dq = deque([])
        for i in range(numCourses):
            if in_deg[i] == 0:
                dq.append(i) # 将入度为0的点加入dq

        visited = 0 # 已经访问的点
        res = [] # 访问的路线
        while dq:
            node = dq.popleft()
            res.append(node)
            visited += 1
            for neib in edge[node]:
                in_deg[neib] -= 1  # 拆掉边node->neib，即入度减1
                if in_deg[neib] == 0:
                    dq.append(neib) # 入度为0的点加入
        # print(res)
        return visited == numCourses

"""
Accepted
49/49 cases passed (40 ms)
Your runtime beats 96.22 % of python3 submissions
Your memory usage beats 55.8 % of python3 submissions (15.6 MB)
"""

# numCourses = 3
# prerequisites = [[0,1],[0,2], [1,0]]      
# s = Solution().canFinish(numCourses, prerequisites)
# print(s)

# @lc code=end

