#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """

#         li = []
#         def DFS(node):
#             if not node:
#                 li.append(None)
#                 return
#             li.append(node.val)
#             DFS(node.left)
#             DFS(node.right)
#         DFS(root)
#         return ','.join([str(i) for i in li])
        

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         data = data.split(',')
#         def dfs(li):
#             try: 
#                 c = data.pop(0)
#             except: # 没数据了，结束
#                 return
#             if c == "None":  # 遇到None，作为节点返回，跳出该层的递归深度
#                 return None
#             c = TreeNode(int(c))  # 先序，先把顶部节点构建起来
#             c.left = dfs(li)      #      再构建其左节点
#             c.right = dfs(li)     #      再构建其右节点
#             return c
#         return dfs(data)
        
"""
Accepted
52/52 cases passed (180 ms)
Your runtime beats 34.95 % of python3 submissions
Your memory usage beats 47.97 % of python3 submissions (19.3 MB)
"""
# 2021-06-30每日一题
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        series = []
        def dfs(node):
            if not node:
                series.append("1001")
                return
            series.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        res = ','.join(series)
        # print(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return 
        
        data = [int(i) for i in data.split(',')]
        data = data[::-1]
        def dfs(li: List):
            if not li:
                return
            num = li.pop()
            if num == 1001:
                return None
            node = TreeNode(num)
            node.left = dfs(li)
            node.right = dfs(li)
            return node
        
        root = dfs(data)
        return root
"""
Accepted
52/52 cases passed (124 ms)
Your runtime beats 91.65 % of python3 submissions
Your memory usage beats 36.91 % of python3 submissions (19.5 MB)
"""
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# data ="1,2,1001,1001,3,4,6,1001,1001,7,1001,1001,5,1001,1001"
# print(data)
# s = Codec().deserialize(data)
# s = Codec().serialize(s)
# print(s)
# @lc code=end

