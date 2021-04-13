#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int):
        res = []
        def backtracking(pth, left, right):
            if left == right == n: # 当左括号数等于右括号数等于n时，记录
                res.append(''.join(pth))
                return
            if left < n:  # 当左括号数小于n时
                pth.append('(') # 添加左括号并进入递归
                backtracking(pth, left+1, right)
                pth.pop() # 回溯这里不太好想n个(后，进入下面的递归，等下面的递归结束有n个)，等下面n个)pop后，(才开始pop，并进入下面递归中。

            if right < left: # 这时已经有left个左括号了，如果右括号比左括号少，就可以添加右括号
                pth.append(')')
                backtracking(pth, left, right+1)
                pth.pop()
        backtracking([], 0, 0)
        return res
"""
Accepted
8/8 cases passed (44 ms)
Your runtime beats 54.89 % of python3 submissions
Your memory usage beats 41.87 % of python3 submissions (15.1 MB)
"""
# @lc code=end

