#
# @lc app=leetcode.cn id=421 lang=python3
#
# [421] 数组中两个数的最大异或值
#

# @lc code=start
class Trie:
    def __init__(self, val):
        self.val = val
        self.children = {}

from typing import List
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        max_num = max(nums)
        L = len(format(max_num, 'b')) - 1 # x>>L后为最高位

        # 构建前缀树
        root = Trie(-1)
        for item in nums:
            curr = root
            for i in range(L, -1, -1):
                v = (item >> i) & 1 # 前面的>>i向右移i位，后面的&1是把最右边那位取出来
                if v not in curr.children: # 不在的话构建下一层
                    curr.children[v] = Trie(v)
                curr = curr.children[v] # 进入下一层

        # 搜索前缀树
        res = -1
        for item in nums:
            curr = root
            total = 0
            for i in range(L, -1, -1):  # 从高位到低位
                v = (item >> i) & 1
                total = total << 1 # 左移一位，空出一个0为当前位，（扩大两倍）
                if 1-v in curr.children: # 如果与其相反的位的数存在的话
                    total = total + 1 # 当前位亦或后为1
                    curr = curr.children[1-v] # 走其相反的
                else: # 不存在与其相反的数
                    # total = total # 当前位亦或后为0，即没变
                    curr = curr.children[v] # 只能走当前路
            res = max(res, total)

        return res

# s = Solution().findMaximumXOR()
"""
Accepted
39/39 cases passed (1512 ms)
Your runtime beats 14.24 % of python3 submissions
Your memory usage beats 5.69 % of python3 submissions (64.3 MB)
"""

# @lc code=end

