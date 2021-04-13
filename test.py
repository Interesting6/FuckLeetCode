# def gen_children(node):
#     li = [[int(i) for i in node] for _ in range(8)]
#     print(li)
#     for i in range(8):
#         li[i][i%4] += (i//4 * 2 - 1)
#         li[i] = [str(j%10) for j in li[i]]
#         li[i] = "".join(li[i])
#     return li

# # print(gen_children("9000"))


# def DFS(node, target, visited: set):
#     if node == target:
#         return True
#     for sub_node in node.children:
#         if sub_node not in visited:
#             visited.add(sub_node)
#             if DFS(sub_node, target, visited) == True:
#                 return True

#     return False


# def DFS(root, target):
#     visited = set()
#     stack = [root, ]
#     while stack:
#         node = stack.pop()
#         if node == target:
#             return True
#         for sub_node in node.children:
#             if sub_node not in visited:
#                 stack.append(sub_node)
#                 visited.append(sub_node)
#     return False



# def f1():
#     res = ""
#     for i in range(10000):
#         res += str(i)
#     # return res

# def f2():
#     res = ""
#     for i in range(10000):
#         res = f"{res}{i}"

# # import timeit
# from timeit import timeit

# print(timeit(f1, number=1000))
# print(timeit(f2, number=1000))

# def main():
#     import sys
#     import io
#     def readlines():
#         for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
#             yield line.strip('\n')

#     lines = readlines()
#     while True:
#         try:
#             line = next(lines)
#             # root = stringToTreeNode(line)
#             print(line)
#             line = next(lines)
#             print(line)
#             # p = int(line)
#             line = next(lines)
#             print(line)
#             # q = int(line)
            
#             print()
#             # ret = Solution().lowestCommonAncestor(root, p, q)

#             # out = treeNodeToString(ret);
#             # print(out)
#         except StopIteration:
#             break

# main()
# from collections import abc
# from typing import List
# import heapq
# import numpy as np
# np.expand_dims

# # np.float
# # np.float32
# # nums = [3,2,3,1,2,4,5,5,6]

# # heapq.heapify(nums)
# # print(nums)


# class Solution:
#     def maxAscendingSum(self, nums):
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         lf = 0
#         rt = 0
#         sum_ = 0
#         res = 0
#         while rt < n:
#             if lf == rt:
#                 sum_ = nums[rt]
#             elif nums[rt-1] < nums[rt]:
#                 sum_ += nums[rt]
#             else:
#                 lf = rt
#                 sum_ = nums[lf]
#             res = max(res, sum_)
#             rt += 1
#         return res

# s = Solution().maxAscendingSum([100, 10, 1])
# print(s)
# from queue import PriorityQueue

# vivo2
# import sys
# def isPalin(s, i, j, k):
#     if i == k:
#         i += 1
#     if j == k:
#         j -= 1
#     if i >= j:
#         return True
#     return s[i]==s[j] and isPalin(s, i+1, j-1, k)

# s = "abda"
# n = len(s)
# if isPalin(s, 0, n-1, -1):
#     print(s)
#     sys.exit(0)

# for p in range(n):
#     if isPalin(s, 0, n-1, p):
#         print(s[:p]+s[p+1:])
#         sys.exit(0)


#vivo3

# n = 15
# sx, sy = 0, 7
# ex, ey = 7, 7

# txt = """
# *5#++B+B+++++$3
# 55#+++++++###$$
# ###$++++++#+*#+
# ++$@$+++$$$3+#+
# +++$$+++$+4###+
# A++++###$@+$++A
# +++++#++$#$$+++
# A++++#+5+#+++++
# +++$$#$++#++++A
# +++$+@$###+++++
# +###4+$+++$$+++
# +#+3$$$+++$##++
# +#*+#++++++#$$+
# $####+++++++$##
# 3$+++B++B++++#5
# """
# matrix = [list(line.strip()) for line in txt.split()]
# # from pprint import pprint
# # pprint(matrix)

# import sys
# block = set("#@")

# queue = [(sx, sy)]
# vis = {(sx, sy)}
# dest = (ex, ey)
# dist = [[0]*n for _ in range(n)]

# step = 0
# while queue:
#     node = queue.pop(0)
#     x, y = node
#     # step += 1
#     step = dist[x][y]
#     if node == dest:
#         print(step)
#         sys.exit(0)
#     for r,c in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
#         if 0<=r<n and 0<=c<n and matrix[r][c] not in block and (r,c) not in vis:
#             queue.append((r,c))
#             vis.add((r,c))
#             dist[r][c] = step + 1
# print(-1)


# inf = float("inf")
# res = inf
# def dfs(x, y, step):
#     global res
#     if (x,y) == dest:
#         res = min(res, step)
#         return
#     for r,c in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
#         if 0<=r<n and 0<=c<n and matrix[r][c] not in block and (r,c) not in vis:
#             vis.add((r, c))
#             dfs(r, c, step+1)
#             vis.remove((r, c))

# dfs(sx, sy, 0)
# if res < inf:
#     print(res)
# else:
#     print(-1)



# vivo1

# nums = [1, 2, -1, 1]
# nums = [5,0,4,4,5,-1]
# nums = [8,2,7,4,6,-1,5,5,6]
# n = len(nums)

# g = [[] for _ in range(n)]
# d = [0] * n

# q = []
# for i in range(n):
#     if nums[i] == -1:
#         q.append(i) # 无依赖的，先处理
#         continue
#     d[i] += 1 # 有依赖
#     g[nums[i]].append(i)


# res = []
# while q:
#     t = q.pop(0)
#     res.append(str(t))
#     for j in g[t]:
#         d[j] -= 1
#         if d[j] == 0:
#             q.append(j)

# def dfs(t):
#     res.append(str(t))
#     parent = g[t]
#     if parent:
#         for i,j in enumerate(parent):
#             dfs(j)

# for t in q:
#     dfs(t)

# res = ','.join(res)
# print(res)


# class Solution:
#     def compileSeq(self , input ):
#         nums = input.split(",")
#         nums = [int(i) for i in nums]
#         n = len(nums)
#         g = [[] for _ in range(n)]
#         d = [0] * n

#         for i in range(n):
#             if nums[i] == -1:
#                 continue
#             d[i] += 1
#             g[nums[i]].append(i)

#         q = []
#         for i in range(n):
#             if not d[i]:
#                 q.append(i)

#         res = []
#         while q:
#             t = q.pop(0)
#             res.append(str(t))
#             for j in g[t]:
#                 d[j] -= 1
#                 if d[j] == 0:
#                     q.append(j)

#         res = ','.join(res)
#         #print(res)
#         return res

# s = Solution().compileSeq("1,2,-1,1")
# print(s)


# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# li = [0,1,2,3,4,5,6,7,None,None,10,11]
# n = len(li)
# j = 0
# q = []
# while j < n:
#     node = TreeNode(li[j])
#     if j == 0:
#         root = node
#         q.append(node)
#     else:
#         if j % 2 ==1:
#             father = q.pop(0)
#             father.left = node
#         else:
#             father.right = node
#         q.append(node)
#     j += 1

# root


# class MulTreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.children = []

# array = [(0, -1), (2, 0), (4, 0), (1, 0), (3, 2), (5, 4), (6, 5), (7, 5)]

# di = {}
# q = []
# for item in array:
#     if item[-1] == -1:
#         node = MulTreeNode(item[0])
#         q.append(node)
#         di[0] = node
#         root = node
#     else:
#         if item[-1] in di:
#             di[item[-1]].children.append(MulTreeNode(item[0]))


# class Solution:
#     def compress(self , str_ ):
#         stack = []
#         digs = set("0123456789")
#         s = ''
#         for c in str_:
#             if c == '[':
#                 if len(s):
#                     stack.append(s)
#                 d = ''
#             elif c == '|':
#                 stack.append(int(d))
#                 stack.append('|')
#                 s = ''
#             elif c in digs:
#                 d += c
#             elif c == ']':
#                 nc = stack.pop()
#                 while nc != '|':
#                     s = nc + s
#                     nc = stack.pop()
#                 d = stack.pop()
#                 s = d * s
#                 stack.append(s)
#                 s = ''
#             else:
#                 s += c
#         if len(s):
#             stack.append(s)
#         print(stack)
#         res = ''.join(stack)
#         print(res)
#         return res


# s = Solution().compress("HG[3|B[2|CA]]F")


# class Solution:
#     def findBuilding(self, heights):
#         n = len(heights)
#         lf = [0] * n
#         rt = [0] * n
#         stack = [heights[0]]
#         for i in range(1, n):
#             lf[i] = len(stack)
#             while stack and heights[i] > stack[-1]:
#                 stack.pop()
#             stack.append(heights[i])
#         stack = [heights[-1]]
#         for i in range(n-2, -1, -1):
#             rt[i] = len(stack)
#             while stack and heights[i] > stack[-1]:
#                 stack.pop()
#             stack.append(heights[i])
#         # print(lf, rt)
#         res = []
#         for i in range(n):
#             res.append(lf[i] + rt[i] + 1)
#         return res
            

# s = Solution().findBuilding([5, 3, 8, 3, 2, 5])
# print(s)

n = 2
li = [2, 1, 4, 3]
m = 4
qli = [1, 2, 0, 2]
pre = None
for i in range(m):
    q = qli[i]
    q = 2**q
    if q == 1 and pre is not None:
        print(pre)
    else:
        


