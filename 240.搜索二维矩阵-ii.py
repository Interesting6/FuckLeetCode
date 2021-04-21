#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
"""关键：遍历对角线，每次从对角线元素出发向下向右"""
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        def bi_search(start, vertical=True):
            lo = start
            hi = m-1 if vertical else n-1
            while lo <= hi: # 好像必须用<=，不然会楼掉
                mid = lo + ((hi-lo)>>1)
                if vertical:
                    if matrix[mid][start] == target:
                        return True
                    elif matrix[mid][start] < target:
                        lo = mid + 1
                    elif matrix[mid][start] > target:
                        hi = mid - 1
                else:
                    if matrix[start][mid] == target:
                        return True
                    elif matrix[start][mid] < target:
                        lo = mid + 1
                    elif matrix[start][mid] > target:
                        hi = mid - 1
            
            return False

        for i in range(min(m, n)):
            col = bi_search(i, True) # 对该列
            row = bi_search(i, False) # 对该行
            if col or row:
                return True
        return False

"""
Accepted
129/129 cases passed (184 ms)
Your runtime beats 73.44 % of python3 submissions
Your memory usage beats 18.7 % of python3 submissions (21 MB)
"""
        
# @lc code=end

