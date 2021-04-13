# @before-stub-for-debug-begin
from python3problem394 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        numset = set("1234567890")
        multi = ''
        res = ''
        for c in s:
            if c in numset: # 为数值时，记录乘子
                multi += c
            elif c == '[': # 为[时，将
                stack.append(int(multi))
                stack.append(res)
                multi = ''
                res = ''

            elif c == ']': # 开始反推
                last_string = stack.pop()
                cur_multi = stack.pop() # 当前的乘子，不能用multi
                res = last_string + cur_multi * res
            else: # 为字母时，得到当前部分的字符串
                res += c
        if stack:
            res = ''.join(stack)

        # print(res)
        return res


# @lc code=end

