# @before-stub-for-debug-begin
from python3problem743 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#

# @lc code=start
"""
深度优先搜索
记录信号到达节点node的时间，到达node时，若时间是最早的，则继续广播该信号；
若该时间不是最早的，说明已经有信号已经到达过该node，后面信号也被前面的信号广播过，所以直接退出该node即可。
"""

# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

#         graph = {} 
#         inf = float("inf")
#         dist = {node: inf for node in range(1, n+1)} # 信号最早到达node的时间

#         for s,d,w in times: # source -> [(neibors,times)]
#             if s not in graph: # w在前方便后面排序
#                 graph[s] = [(w, d)]
#             else:
#                 graph[s].append((w, d))
        
#         def dfs(node, elapsed):
#             if elapsed >= dist[node]: # 现在到node花的时间比之前到node花的时间还长，直接退出该路线
#                 return
#             # 最早到node：现在到node花的时间比之前到node花的时间更少，所以更新
#             dist[node] = elapsed
#             neibourstime = graph.get(node, [])
#             for w, neib in sorted(neibourstime):
#                 dfs(neib, elapsed+w)
            
#         dfs(k, 0)
#         res = max(dist.values())
#         if res < inf:
#             return res
#         else:
#             return -1


# """Dijkstra's Algorithm"""
# class Solution:
#     def networkDelayTime(self, times, n, k):
#         import collections
#         inf = float("inf")
#         graph = collections.defaultdict(list)
#         for sc, de, tm in times:
#             graph[sc].append((de, tm)) 
            
#         dist = { i: inf for i in range(1, n+1) } # k到node的最短距离
#         seen = [0] * (n+1)
#         # seen[k] = 1 不能加这个，因为一开始要先到k自己，距离为0。
#         # 第一次找到的cand_node为k自己，然后再从k出发查找！！！
#         dist[k] = 0
#         while True:
#             cand_node = -1
#             k2_cand_node_dist = inf
#             for i in range(1, n+1): # 遍历1到n，找距离k最近的candidate
#                 if not seen[i] and dist[i] < k2_cand_node_dist:
#                     k2_cand_node_dist = dist[i] # 距k最近节点的距离
#                     cand_node = i # 最近的candidate节点
#             if cand_node < 0: # 没找到
#                 break
#             seen[cand_node] = 1 # 将其设为访问过
#             # 更新k到cand_node邻居的距离？
#             # 是从k中途经过cand_node到邻居neib的路线时间短
#             # 还是从k未经过cand_node到邻居neib的时间短？更新为那个更小的
#             for neib, tm in graph[cand_node]:
#                 dist[neib] = min(dist[neib], dist[cand_node]+tm)
#         res = max(dist.values())
#         if res == inf:
#             return -1
#         return res


"""Dijkstra's Algorithm，改编一下"""
# class Solution:
#     def networkDelayTime(self, times, n, k):
#         import collections
#         inf = float("inf")
#         graph = collections.defaultdict(list)
#         for sc, de, tm in times:
#             graph[sc].append((de, tm)) 
            
#         dist = { i: inf for i in range(1, n+1) } # k到node的最短距离
#         seen = [0] * (n+1)
#         # seen[k] = 1 不能加这个，因为一开始要先到k自己，距离为0。
#         # 第一次找到的cand_node为k自己，然后再从k出发查找！！！
#         dist[k] = 0

#         def get_shortest_dist_node(dist):
#             cand_node = None
#             k_2_cand_node_dist = inf
#             for i in range(1, n+1): # 遍历1到n，找距离k最近的candidate
#                 if not seen[i] and dist[i] < k_2_cand_node_dist: # 没走过，且开销更低
#                     k_2_cand_node_dist = dist[i] # 距k最近节点的距离
#                     cand_node = i # 距离k最近的candidate节点（当前开销最小的）
#             return cand_node

#         node = get_shortest_dist_node(dist)
#         while node: # 若还有当前离起点最近的节点
#             seen[node] = 1 # 将其设为访问过
#             # 更新到其邻居的开销
#             cur_node_tm = dist[node] 
#             for neib_node, neib_tm in graph[node]:
#                 new_tm = cur_node_tm + neib_tm # 经过node到达neib_node的时间
#                 if new_tm < dist[neib_node]: # 若经过node到达neib_node更短，则更新时间
#                     dist[neib_node] = new_tm
#             node = get_shortest_dist_node(dist)

#         res = max(dist.values())
#         if res == inf:
#             return -1
#         return res


"""堆实现"""
# class Solution:
#     def networkDelayTime(self, times, n, k):
#         import heapq
#         from collections import defaultdict
#         dist = {} # 初始化为空，表示全部没访问过
#         graph = defaultdict(list)
#         for sc, de, tm in times:
#             graph[sc].append((de, tm))
#         hp = [(0, k)] # 初始化从k到第k个点耗时为0，
#         while hp:
#             tm, node = heapq.heappop(hp) # 把没访问的，下一个访问最早的推出来
#             if node not in dist: # 之前没被访问过
#                 dist[node] = tm  # 现在访问一定是最短时间的
#             for neib, neibtm in graph[node]:
#                 if neib not in dist: # 把没有被访问的邻居推入堆，注意时间要加上当前的时间，表示从k出发到该neib所需时间
#                     heapq.heappush(hp, (tm+neibtm, neib))
#         res = max(dist.values())
#         if len(dist) == n: # 全部访问了
#             return res
#         else:  # 还有节点没访问到，返回-1
#             return -1


# 隔天第二次做，感觉白做了。。上面一种都想不起来。。。
# class Solution:
#     def networkDelayTime(self, times, n, k):
#         from collections import defaultdict
#         import heapq
#         graph = defaultdict(list)
#         for sc, dst, tm in times:
#             graph[sc].append((tm, dst))
#         inf = float("inf")
#         dist = {}
#         hp = [(0, k)]
#         while hp:
#             tm, node = heapq.heappop(hp)
#             if node not in dist:
#                 dist[node] = tm
#             for ntm, neib in graph[node]:
#                 if neib not in dist:
#                     heapq.heappush(hp, (tm+ntm, neib))
#         res = max(dist.values())
#         if len(dist) == n:
#             return res
#         else:
#             return -1


# 21-04-04 第3次做，大部分还是都忘了。。
# class Solution:
#     def networkDelayTime(self, times, n, k):
#         from collections import defaultdict
#         import heapq
#         graph = defaultdict(list)
#         for sc, ds, tm in times:
#             graph[sc].append((tm, ds))
        
#         dist = {}
#         hp = [(0, k)]
#         while hp:
#             tm, node = heapq.heappop(hp)
#             if node not in dist:
#                 dist[node] = tm
#             for nei_tm, nei_nd in graph[node]:
#                 if nei_nd not in dist:
#                     heapq.heappush(hp, (tm+nei_tm, nei_nd))
#         if len(dist) == n:
#             return max(dist.values())
#         else:
#             return -1

# 21-04-08 第4次做，终于会做了。。。。
# class Solution:
#     def networkDelayTime(self, times, n, K):
#         from collections import defaultdict
#         graph = defaultdict(list)
#         for sc, ds, tm in times:
#             graph[sc].append((tm, ds))
#         dist = {}
#         hp = [(0, K)]
#         import heapq
#         while hp:
#             tm, node = heapq.heappop(hp)
#             if node not in dist:
#                 dist[node] = tm
#             for neib_tm, neib in graph[node]:
#                 if neib not in dist:
#                     heapq.heappush(hp, (tm+neib_tm, neib))
#         if len(dist) != n:
#             return -1
#         else:
#             res = max(dist.values())
#             return res

# class Solution:
#     """dfs的解法也通过，只需让访问比之前访问的时间小就继续传播即可"""
#     def networkDelayTime(self, times, n, K):
#         from collections import defaultdict
#         graph = defaultdict(list)
#         for sc, ds, tm in times:
#             graph[sc].append((tm, ds))
#         inf = float("inf")
#         dist = {i:inf for i in range(1, n+1)} # 初始化访问为无穷大，代表没访问
#         dist[K] = 0
#         def dfs(node, usetm):
#             for neib_tm, neib in graph[node]:
#                 if usetm+neib_tm < dist[neib]:
#                     dist[neib] = usetm+neib_tm
#                     dfs(neib, dist[neib])
#         dfs(K, 0)
#         res = max(dist.values())
#         if res == inf:
#             return -1
#         else:
#             return res


# @lc code=end

