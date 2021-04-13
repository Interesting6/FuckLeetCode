#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_cnt = Counter(magazine)
        magazine_cnt.subtract(ransomNote)
        t = list(filter(lambda x: x[1] <0, magazine_cnt.items()))
        return len(t) == 0
"""
Accepted
129/129 cases passed (52 ms)
Your runtime beats 85.61 % of python3 submissions
Your memory usage beats 52.19 % of python3 submissions (15 MB)
"""
# @lc code=end

