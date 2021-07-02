#
# @lc app=leetcode.cn id=483 lang=python3
#
# [483] 最小好进制
#

# @lc code=start
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        def check(x, m):
            ans = 0
            for _ in range(m+1):
                ans = ans * x + 1
            return ans
        
        ans = float("inf")
        for i in range(1, 64):
            l, r = 2, num
            while l < r:
                mid = l + ((r - l) >> 1)
                tmp = check(mid, i)
                if tmp == num:
                    ans = min(ans, mid)
                    break
                elif tmp < num:
                    l = mid + 1
                elif tmp > num:
                    r = mid
        return str(ans)
"""
Accepted
106/106 cases passed (976 ms)
Your runtime beats 8 % of python3 submissions
Your memory usage beats 6 % of python3 submissions (15 MB)
"""
# s = Solution().smallestGoodBase(13)
# print(s)

# @lc code=end

