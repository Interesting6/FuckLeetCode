#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mp = {chr(65+i): (i+1) for i in range(26)}
        res = 0
        for c in columnTitle:
            res = (res * 26) + mp[c]

        return res
"""
Accepted
1002/1002 cases passed (44 ms)
Your runtime beats 53.71 % of python3 submissions
Your memory usage beats 5.38 % of python3 submissions (15 MB)
"""
# res = Solution().titleToNumber("AB")
# print(res)
# @lc code=end

