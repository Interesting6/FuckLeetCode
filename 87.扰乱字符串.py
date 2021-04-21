#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#

# @lc code=start
class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        N = len(s1)
        if N == 0:
            return True
        elif N == 1:
            return s1 == s2
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, N):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            elif self.isScramble(s1[:i], s2[-i:]) and \
                self.isScramble(s1[i:], s2[:-i]):
                return True
        return False

"""
s1[0:i]和 s2[0:i]作为左子树，s1[i:N]和 s2[i:N]作为右子树
s1[0:i]和 s2[N - i:N]作为左子树，s1[i:N]和 s2[0:N-i]作为右子树
Accepted
288/288 cases passed (40 ms)
Your runtime beats 97.57 % of python3 submissions
Your memory usage beats 9.54 % of python3 submissions (16.5 MB)
"""     


# @lc code=end

