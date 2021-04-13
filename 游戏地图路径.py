
text = """
*5#++B+B+++++$3
55#+++++++###$$
###$++++++#+*#+
++$@$+++$$$3+#+
+++$$+++$+4###+
A++++###$@+$++A
+++++#++$#$$+++
A++++#+5+#+++++
+++$$#$++#++++A
+++$+@$###+++++
+###4+$+++$$+++
+#+3$$$+++$##++
+#*+#++++++#$$+
$####+++++++$##
3$+++B++B++++#5
"""

matrix = text.strip().split()
matrix = [list(line.strip()) for line in matrix]
n = len(matrix)

sx, sy = 7, 0
ex, ey = 7, 7

inf = float("inf")
blocks = set("#@")
import sys


# 广度优先
dist = [[0]*n for _ in range(n)]
vis = set([(sx, sy)])
queue = [(sx, sy)]
while queue:
    x, y = queue.pop(0)
    if (x, y) == (ex, ey):
        print(dist[x][y])
        # print(dist)
        sys.exit(0)
    for r, c in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0<=r<n and 0<=c<n and matrix[r][c] not in blocks and (r,c) not in vis:
            queue.append((r, c))
            vis.add((r, c))
            dist[r][c] = dist[x][y] + 1

print(-1) # 到达不了


# 深度优先
# inf = float("inf")
# dist = [[inf]* n for _ in range(n)]
# def dfs(x, y, step):
#     dist[x][y] = step
#     if (x, y) == (ex, ey):
#         return
#     for r, c in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
#         if 0<=r<n and 0<=c<n and matrix[r][c] not in blocks: # 可以走
#             if step + 1 < dist[r][c]: # 比之前到r,c的路径短，更新路径
#                 dfs(r, c, step+1)
#             else:
#                 pass
        
# dfs(sx, sy, 0)
# if dist[ex][ey] == inf:
#     print(-1)
#     import sys
#     sys.exit(0)
# print(dist[ex][ey])
