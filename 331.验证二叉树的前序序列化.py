# @before-stub-for-debug-begin
from python3problem331 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
"""栈中#消去"""
# class Solution:
#     def isValidSerialization(self, preorder: str) -> bool:
#         stack = []
#         preorder = preorder.split(',')
#         for c in preorder:
#             stack.append(c)
#             while len(stack)>=3 and stack[-2] == stack[-1] == '#' and stack[-3]!='#':
#                 # 当出现d##时，消去d为#
#                 stack.pop()
#                 stack.pop()
#                 stack[-1] = '#'
#         return len(stack)==1 and stack.pop() == '#'
# """Accepted
# 150/150 cases passed (48 ms)
# Your runtime beats 30.31 % of python3 submissions
# Your memory usage beats 74.28 % of python3 submissions (14.7 MB)"""

"""计算出入度"""
class Solution:
    def isValidSerialization(self, preorder):
        diff = 1
        for c in preorder.split(','):
            diff -= 1 #当一个节点进来时，先减去一个入度
            if diff < 0: # 还没遍历到该节点的子节点，此时出度应该大于等于入度
                return False # 一定要注意这个if放在-入度和+出度之间！！！
            if c != '#': # 非空节点
                diff += 2 # 增加2个出
            else:  # 空节点，无出度
                pass
            
        if diff == 0:
            return True
        else:
            return False

# @lc code=end

