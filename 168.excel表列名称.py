#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mp = {i: chr(65+i) for i in range(26)}
        from collections import deque
        res = deque([])

        while columnNumber: # 商不为0，可以继续求模
            columnNumber, r = divmod(columnNumber-1, 26) 
            res.appendleft(mp[r])

        res = "".join(res)
        return res
""" 
Accepted
18/18 cases passed (40 ms)
Your runtime beats 59.63 % of python3 submissions
Your memory usage beats 5.14 % of python3 submissions (15.1 MB)
"""
# res = Solution().convertToTitle(2147483647)
# print(res)

# @lc code=end

