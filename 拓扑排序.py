

# G = {
#     'a':'bf',
#     'b':'cdf',
#     'c':'d',
#     'd':'ef',
#     'e':'f',
#     'f':''
# }


# def topoSort(graph):
#     in_degrees = dict((u, 0) for u in graph) # 初始化所有顶点的入度为0
#     n = len(in_degrees)
#     for u in graph:
#         for v in graph[u]: # 有u→v，即有u指向v，v的入度要＋1
#             in_degrees[v] += 1 # 计算每个顶点的入度

#     Q = [u for u in in_degrees if in_degrees[u] == 0] # 筛选入度为0的顶点
#     Seq = []
#     while Q:
#         u = Q.pop()
#         Seq.append(u)
#         for v in graph[u]:
#             in_degrees[v] -= 1 # 删除其所有边？指向v的数量减一，即删除u->v的连接
#             if in_degrees[v] == 0: # v入度为0了
#                 Q.append(v)   # 加入Q中
#     if len(Seq) == n: # 顶点数与图中点的个数相等
#         return Seq
#     else:
#         return -1

# res = topoSort(G)
# print(res)


class Solution:
    def compileSeq(self , nums):
        from collections import defaultdict
        nums = [int(i) for i in nums.split(",")]
        graph = defaultdict(list)  # k: v 为k -> v，v依赖于k，v入度为1
        Q = []
        for i, num in enumerate(nums): # num->i， i需要依赖于num
            graph[num].append(i)
            if num == -1: # i无依赖
                Q.append(i)
        n = len(nums)
        in_degrees = {
            u: 0 for u in range(n)
        } # 初始化入度为0
        for u in graph:
            for v in graph[u]: # u->v
                in_degrees[v] += 1

        res = []
        while Q:
            u = Q.pop(0)
            res.append(str(u))
            for v in graph[u]: # u->v 表示u所连接的v
                in_degrees[v] -= 1 # 删掉u-v这个边，v的入度就减少1
                if in_degrees[v] == 0: # 入度为0
                    Q.append(v)
        res = ",".join(res)
        return res
            

# s = Solution().compileSeq("1,2,-1,1") 
s = Solution().compileSeq("5,0,4,4,5,-1")         
print(s)




