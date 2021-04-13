# @before-stub-for-debug-begin
from python3problem224 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = "(1+(4+5+2)-3)+(6+8)"
        s = '(' + s + ')'
        stack = []
        dig = "1234567890"
        opr = "+-"
        d = ''
        for c in s:
            if c != ' ':
                if c in '(+-':
                    if d != '':
                        if stack and stack[-1] == '-':
                            d = -int(d)
                            stack[-1] = d
                        else:
                            stack.append(int(d))
                        d = ''
                    if c in '(-':
                        stack.append(c)
                elif c in dig:
                    d += c
                elif c == ')':
                    if stack and stack[-1] == '-':
                        d = -int(d)
                        stack.pop()
                    else:
                        d = int(d)
                    op = stack.pop()
                    while op != '(':
                        d = op + d
                        op = stack.pop()
        print(d)
        return d
# @lc code=end

