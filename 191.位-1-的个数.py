# @before-stub-for-debug-begin
from python3problem191 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)[2:]
        return sum([int(i) for i in s])
# @lc code=end

