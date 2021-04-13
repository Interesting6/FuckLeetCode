#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        n = len(strs)
        if n == 0:
            return res
        i = -1
        di = {}
        for item in strs:
            key = tuple(sorted(item))
            if key in di:
                idx = di[key]
                res[idx].append(item)
            else:
                res.append([item])
                i += 1
                di[key] = i
        return res
""" 每个字符串都sort一遍居然还能过
Accepted
114/114 cases passed (60 ms)
Your runtime beats 62.52 % of python3 submissions
Your memory usage beats 22.61 % of python3 submissions (18.3 MB)
"""
# @lc code=end

