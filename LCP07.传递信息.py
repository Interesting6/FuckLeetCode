from collections import defaultdict
from typing import List

class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for s, d in relation:
            graph[s].append(d)
        print(graph)
        res = 0
        def dfs(node, step):
            if step == k:
                if node == n-1:
                    nonlocal res
                    res += 1
                return
            for new_node in graph[node]:
                dfs(new_node, step+1)
            
        dfs(0, 0)
        return res
        
n = 5; relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]; k = 3
s = Solution().numWays(n, relation, k)
print(s)