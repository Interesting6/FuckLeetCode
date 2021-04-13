#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if n <= 2:
            return True
        else:
            inc = None
            dec = None
            for i in range(1, n):
                if A[i-1] < A[i]:
                    inc = True
                    if dec is not None:
                        return False
                elif A[i-1] > A[i]:
                    dec = True
                    if inc is not None:
                        return False
                else:
                    pass
        return True
        
# @lc code=end

