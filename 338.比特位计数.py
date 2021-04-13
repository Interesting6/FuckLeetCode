# @before-stub-for-debug-begin
from python3problem338 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        cache = {0:0, 1:1, 2:2}
        res = []
        for x in range(num+1):
            if x == 0:
                res.append(0)
                continue
            if x % 2 != 0: # 奇数情况时为前面的偶数+1
                cache[x] = cache[x-1] + 1
                res.append(cache[x])
            else:
                # 偶数情况时等于对应的奇数
                cache[x] = cache[x//2]
                res.append(cache[x])
        return res
        
# @lc code=end

