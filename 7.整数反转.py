# @before-stub-for-debug-begin
from python3problem7 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            x = -x
            flag = True
        y = 0
        bound = 2**31
        while x!=0:
            if y< -bound or y>bound-1:
                return 0
            y = y*10 + x%10 # y右边加0 + x的个位数
            x = x // 10 
        if flag:
            y = -y
        if y<-bound or y>bound-1:
            return 0
        return y

# @lc code=end

