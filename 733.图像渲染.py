#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start



class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        h = len(image)
        w = len(image[0])
        t = image[sr][sc]
        vis = set()
        def DFS(r, c):
            if image[r][c] == t and (r, c) not in vis:
                image[r][c] = newColor
                vis.add((r, c))
                if 0 <= r-1:
                    DFS(r-1, c)
                if r+1 < h:
                    DFS(r+1, c)
                if 0 <= c-1:
                    DFS(r, c-1)
                if c+1 < w:
                    DFS(r, c+1)
        DFS(sr, sc)
        return image  

        
# @lc code=end

