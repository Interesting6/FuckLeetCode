# @before-stub-for-debug-begin
from python3problem227 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start

def calc(nums, ops):
    if len(nums) < 2:
        return
    if not ops:
        return
    b = nums.pop()
    a = nums.pop()
    op = ops.pop()
    if op == '+':
        ans = a + b
    elif op == '-':
        ans = a - b
    elif op == '*':
        ans = a * b
    elif op == '/':
        ans = a // b
    elif op == '^':
        ans = a ** b
    elif op == '%':
        ans = a % b
    else:
        raise ValueError
    nums.append(ans)

class Solution:
    def calculate(self, s: str) -> int:
        prio = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '%': 2,
            '^': 3,
        }
        nums = [0,]
        ops = []
        digs = "0123456789"
        opset = "+-*/%^"
        preSign = '+'
        d = ''
        for c in s:
            if c != ' ':
                if c in digs: # 数字
                    d += c
                else:
                    nums.append(int(d))
                    d = ''

                    if c == '(':
                        ops.append(c)
                    elif c == ')':
                        while ops:  # 计算到最近的一个左括号为止
                            if ops[-1] != '(':
                                calc(nums, ops)
                            else:
                                ops.pop() # 把'(‘删除
                                break
                    elif c in opset: # 有一个新操作符入栈时，把栈内可以算的都算了
                        while ops and ops[-1]!='(': #当栈内不为空或无左括号
                            prev = ops[-1]
                            if prio[prev] >= prio[c]: # 前一个运算符优先级大于等于当前运算符
                                # 比如当前是-，前面是*或-，先把前面算完。
                                calc(nums, ops)
                            else:
                                break
                        ops.append(c)
        if d != '':
            nums.append(int(d))
        while ops:
            calc(nums, ops)
        return nums[-1]
""" 基本上是万能计算器了
Accepted
109/109 cases passed (120 ms)
Your runtime beats 35.52 % of python3 submissions
Your memory usage beats 99.22 % of python3 submissions (14.9 MB)
"""

# @lc code=end

