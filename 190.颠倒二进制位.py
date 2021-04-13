#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res<<1) | (n&1) # res左移一位（末尾必然是0），并把n末尾一位加进来
            n = n >> 1  # n把末尾的数删除
        return res
# @lc code=end

