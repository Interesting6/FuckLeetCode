#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m , n = len(board), len(board[0])
        store = []
        def dfs(i, j):
            board[i][j] = "1"
            store.append((i, j))
            for r,c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0<=r<m and 0<=c<n and board[r][c] == "O":
                    dfs(r, c)
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n-1] == "O":
                dfs(i, n-1)
        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m-1][j] == "O":
                dfs(m-1, j)
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i,j in store:
            board[i][j] = "O"


# @lc code=end

