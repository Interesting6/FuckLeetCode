#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, k):
            if i<0 or i>=m or j<0 or j>=n: # 边界外、越界了
                return False
            if board[i][j] != word[k]: # 与目标值不同，或者已经访问过了
                return False
            if k == len(word) - 1: # 找到了
                return True
            board[i][j] = '#' # 是word[k]，将其mark为已访问
            res = False
            for x,y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                res = res or dfs(x, y, k+1)
            board[i][j] = word[k] # 回溯，在这层里，把该元素标记回去
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]: # 找到起始点
                    if dfs(i, j, 0): # 从该起始点开始深度搜索
                        return True
        return False

        
# @lc code=end

