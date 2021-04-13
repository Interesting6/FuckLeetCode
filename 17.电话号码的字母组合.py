#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        pth = []
        n = len(digits)
        if n==0:
            return res
        di = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
            "6":"mno", "7":"pqrs", "8": "tuv", "9":"wxyz"}
        def backtracking(depth):
            if depth == n:
                res.append(''.join(pth))
                return
            s = di[digits[depth]]
            for c in s:
                pth.append(c)
                backtracking(depth+1)
                pth.pop()
        backtracking(0)
        return res
        
"""
Accepted
25/25 cases passed (28 ms)
Your runtime beats 98.35 % of python3 submissions
Your memory usage beats 78.21 % of python3 submissions (14.8 MB)
"""
# @lc code=end

