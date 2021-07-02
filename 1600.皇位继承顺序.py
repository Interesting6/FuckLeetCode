#
# @lc app=leetcode.cn id=1600 lang=python3
#
# [1600] 皇位继承顺序
#

# @lc code=start
from typing import List
from collections import defaultdict
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.edges = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.edges[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = list()
        def preorder(name: str) -> None:
            if name not in self.dead:
                ans.append(name)
            if name in self.edges:
                for childName in self.edges[name]:
                    preorder(childName)

        preorder(self.kingName)
        return ans
""" 本质是一个多叉树的前序遍历？？？没搞懂。。6.20打卡题
Accepted
49/49 cases passed (520 ms)
Your runtime beats 82.14 % of python3 submissions
Your memory usage beats 75 % of python3 submissions (63.7 MB)
"""

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
# @lc code=end

