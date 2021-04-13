#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.cnt = n

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] > self.size[rootQ]:
            # 注意这里的指向跟链表的当前指针指向相反！！
            self.parent[rootQ] = rootP # 这里是用=左边的父节点指向=后面的
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]
        self.cnt -= 1

    def find(self, i):
        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    uf.union(i, j)
        return uf.cnt

"""
Accepted
113/113 cases passed (60 ms)
Your runtime beats 52.89 % of python3 submissions
Your memory usage beats 38.99 % of python3 submissions (15.2 MB)
"""

# @lc code=end

