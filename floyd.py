text = """
    4 8
    1 2 2
    1 3 6
    1 4 4
    2 3 3
    3 1 7
    3 4 1
    4 1 5
    4 3 12
"""

text = text.strip().split("\n")
n, m = text[0].strip().split() # 顶点个数、边的个数
n, m = int(n), int(m)
edges = [
    [ int(i) for i in line.strip().split()] \
        for line in text[1:]
]
print(edges)

def floyd(node, edges):
    inf = float("inf")
    dist = [[inf]*node for _ in range(node)]
    for sc, ds, v in edges:
        dist[sc-1][ds-1] = v
    for i in range(node):
        dist[i][i] = 0
    
    for k in range(node): # 经过k中转
        for i in range(node):
            for j in range(node):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist

dist = floyd(n, edges)
from pprint import pprint
pprint(dist)
