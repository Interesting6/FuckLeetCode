# @before-stub-for-debug-begin
from python3problem10 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: # p为空时
            return not s # s也必须为空，才正确匹配完

        # 第一个字符匹配成功，即p与s的第一个字符相等或p[0]为'.'
        first_matched = len(s)>0 and (p[0] in {s[0], '.'}) 

        if len(p) >= 2 and p[1] == "*": # 发现p中的*通配符
            not_used = self.isMatch(s, p[2:]) # *没起到作用，直接跳过p中的该两个字符$*，而s不跳。
            used = first_matched and self.isMatch(s[1:], p) # *起到作用，p的$*将s[0]匹配掉了，递归调用，以进行是否继续匹配
            # 出现*时，可以使用，也可以不使用。
            return not_used or used
        else: # 没有*的情况，只匹配p和s的第一个字符
            return first_matched and self.isMatch(s[1:], p[1:])
# @lc code=end

