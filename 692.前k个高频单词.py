#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#

# @lc code=start
from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        cnt = Counter(words)
        res = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
        res = [i[0] for i in res[:k]]
        return res
        
"""
Accepted
110/110 cases passed (72 ms)
Your runtime beats 42.74 % of python3 submissions
Your memory usage beats 55.43 % of python3 submissions (15 MB)
"""

# @lc code=end

