#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self,):
        self.vis = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        if node in self.vis: # 若被访问过，则直接从hash表中取出
            return self.vis[node]
        
        clone_node = Node(node.val, []) # 复制节点，为了深拷贝，故不克隆其邻居

        self.vis[node] = clone_node # 存储到哈希表

        # 遍历该节点的邻居并更新克隆节点的邻居列表
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node


        
# @lc code=end

