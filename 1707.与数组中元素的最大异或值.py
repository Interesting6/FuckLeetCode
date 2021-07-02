#
# @lc app=leetcode.cn id=1707 lang=python3
#
# [1707] 与数组中元素的最大异或值
#

# @lc code=start
class Trie:
    def __init__(self, val):
        self.val = val
        self.children = {}

from typing import List
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        length = len(nums)
        nums.sort()
        queries = [(queries[i][0], queries[i][1], i) for i in range(len(queries))]
        queries.sort(key=lambda x: x[1])
        max_n = nums[-1]
        L = len(format(max_n, "b")) - 1
        # 建树
        def add(root, n):
            cur = root
            for i in range(L, -1, -1):
                v = (n >> i) & 1
                if v not in cur.children:
                    cur.children[v] = Trie(v)
                cur = cur.children[v]

        def check(root, x):
            try:
                cur = root
                res = 0
                for i in range(L, -1, -1):
                    v = (x >> i) & 1
                    res = res << 1
                    if 1-v in cur.children:
                        res += 1
                        cur = cur.children[1-v]
                    else:
                        cur = cur.children[v]

                j = L + 1
                Lx = len(format(x, 'b'))
                while j < Lx: # 还有高位
                    res = (1 << j) | res
                    j += 1
                return res
            except:
                return -1

        
        root = Trie(-1)
        ans = []
        j = 0
        for x, m, i in queries:
            while j<length and nums[j] <= m: 
                add(root, nums[j])
                j += 1
            x_res = check(root, x)
            ans.append((x_res, i))
        ans.sort(key=lambda x: x[1])
        ans = [it[0] for it in ans]
        return ans


# nums = [5,2,4,6,6,3]; queries = [[12,4],[8,1],[6,3]]
# s = Solution().maximizeXor(nums, queries)
# print(s)

# @lc code=end

