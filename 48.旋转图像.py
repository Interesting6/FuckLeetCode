#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        while i < n // 2:
            d = n - 2*i
            # swap(matrix[i][i:i+d], matrix[i:i+d][n-1-i])
            # swap(matrix[i][i:i+d], matrix[n-1-i][n-1-i:i:-1])
            # swap(matrix[i][i:i+d], matrix[n-1-i:i:-1][i])
            for j in range(d-1):
                # 交换上与右：顺序相同(都是顺)，上从左到右，右从上到下
                matrix[i][i+j], matrix[i+j][n-1-i] =  matrix[i+j][n-1-i], matrix[i][i+j]
                # 交换下与左：顺序相同(都是逆)，下从右到左，左从下到上
                matrix[n-1-i][n-1-i-j], matrix[n-1-i-j][i] = matrix[n-1-i-j][i], matrix[n-1-i][n-1-i-j]
                # 逆序交换上与下，顺序相反：上从左到右，下从右到左
                matrix[i][i+j], matrix[n-1-i][n-1-i-j] = matrix[n-1-i][n-1-i-j], matrix[i][i+j]
            i += 1
        # print(matrix)
        return

# s = Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])
"""
Accepted
21/21 cases passed (32 ms)
Your runtime beats 94.64 % of python3 submissions
Your memory usage beats 37.92 % of python3 submissions (14.9 MB)
"""
# @lc code=end

