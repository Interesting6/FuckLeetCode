# @before-stub-for-debug-begin
from python3problem765 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=765 lang=python3
#
# [765] 情侣牵手
#

# @lc code=start
"""贪心算法"""
# class Solution:
#     def minSwapsCouples(self, row: List[int]) -> int:
#         num_row = len(row)
#         N = num_row // 2
#         res = 0
#         for i in range(0, num_row, 2): # 遍历情侣座的偶数位置(其实从1开始数就是奇数位置)
#             # 即遍历每个情侣座位对中的第一个位置
#             if row[i] == row[i+1] ^ 1: # 当前情侣座的第一个人与第二个人是情侣
#                 continue # 直接跳出
#             # 否者往i+1后面找，直到找到其情侣，找到后交换位置
#             for j in range(i+1, num_row): # i后面的每一个位置
#                 if row[i] == row[j] ^ 1: # 找到了i的情侣
#                     row[i+1], row[j] = row[j], row[i+1] # 交换该情侣座第二个位置
#                     break # 找到了就break
#             res += 1 # 交换的结果加一
#         return res
# """
# Accepted
# 56/56 cases passed (44 ms)
# Your runtime beats 50.81 % of python3 submissions
# Your memory usage beats 71.57 % of python3 submissions (14.8 MB)
# """

"""
并查集：
一堆中k对情侣，互相做错了位置，得进行k-1次交换才能全坐对。
累加最少交换次数：
(n1 - 1) + (n2 - 1) + .....
每个“一堆”都需要 - 1，累加起来就是有几个“一堆”的总数；n1 + n2 + ... 也就是总情侣的个数；那么最少交换次数的公式就：
情侣总数 - “一堆”情侣总数，使用了并查集，也就是情侣总数 - 并查集个数
故要从N对情侣中，找出堆数。
由于2*n与2*n+1配对，所以两个编号除以2应对应同一个数字
"""
class UnionFind:
    def __init__(self, n):
        self.arr = list(range(n)) # 每个元素(节点i)的所属连通区域(父节点)
        self.size = [1] * n # 每个连通量的重量
        self.cnt = n # 不连通量

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j: # 两个属于同一个连通分量
            return
        else: # 两个属于不同连通分量，将他们连通到一起
            # 平衡性优化：
            if self.size[root_i] > self.size[root_j]: # rootj更小，
                self.arr[root_j] = root_i # 将rootj放在rooti下，即rootj的父节点为rooti
                self.size[root_i] += self.size[root_j] # 把rootj的节点加入rooti的节点
            else:
                self.arr[root_i] = self.arr[root_j] # 注意这步的顺序
                self.size[root_j] += self.size[root_i]
            self.cnt -= 1 # 连通分量数量减一

    def find(self, i):
        # 在一个连通区域内，只有在根节点其parent才为自身
        while self.arr[i] != i: # 递归查找i的根节点
            self.arr[i] = self.arr[self.arr[i]] # 路径压缩
            i = self.arr[i] # 指向其父节点，继续查找
        return i

class Solution:
    def minSwapsCouples(self, row):
        num_row = len(row)
        N = num_row // 2
        uf = UnionFind(N)
        for i in range(0, num_row, 2): # 对每个情侣座的第一个位置
            uf.union(row[i]//2, row[i+1]//2) 
            # 如果该情侣座两个人是情侣(属于同一连通区域)，则不操作，他们就是独立一堆；
            # 否者该情侣座不是属于一个连通区域，让他们连通为一堆
        return N - uf.cnt


# @lc code=end

