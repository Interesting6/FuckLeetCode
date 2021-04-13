# @before-stub-for-debug-begin
from python3problem150 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
import math
def calculate(a, b, x):
    if x == '+':
        return a + b
    elif x == '-':
        return a - b
    elif x == '*':
        return a * b
    else:
        if a * b > 0:
            return a // b
        elif a < 0:
            return -(-a // b)
        else:
            return -(a // -b) 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # res = 0
        for x in tokens:
            if x not in "+-*/":
                stack.append(int(x))
            else:
                a = stack.pop()
                stack[-1] = calculate(stack[-1], a, x)
            # print(stack)
        return stack.pop()

# @lc code=end

