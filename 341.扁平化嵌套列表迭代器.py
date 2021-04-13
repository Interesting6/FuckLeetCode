# @before-stub-for-debug-begin
from python3problem341 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=341 lang=python3
#
# [341] 扁平化嵌套列表迭代器
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

"""nestedList为pythonlist的时候，该程序可通过"""
# class NestedIterator:
#     def __init__(self, nestedList):
#         self.gen = nestedList
#         self.stack = []
    
#     def next(self) -> int:
#         if self.hasNext():
#             if self.stack:
#                 first_ele = self.stack.pop()
#             else:
#                 first_ele = self.gen.pop(0)
#             while not isinstance(first_ele, int):
#                 inner_ele = first_ele.pop(0)
#                 if first_ele:
#                     self.stack.append(first_ele)
#                 first_ele = inner_ele
#             return first_ele
    
#     def hasNext(self) -> bool:
#         if self.gen or self.stack:
#             return True
#         else:
#             return False


class NestedIterator:
    def __init__(self, nestedList):
        print(nestedList)
        from collections import deque
        self.que = deque()
        def dfs(li):
            if not li:
                return
            for item in li:
                if item.isInteger():
                    self.que.append(item.getInteger())
                else:
                    li = item.getList()
                    dfs(li)
        dfs(nestedList)                

    def next(self) -> int:
        return self.que.popleft()
    
    def hasNext(self) -> bool:
        return len(self.que)


# s = NestedIterator([[1,1,[2,2,2,[1,3, [2,4]], 2], 1,], [2,3,[4,5],3,2]])
# while s.hasNext():
#     print(s.next())
        
# @lc code=end
"""
[
    NestedInteger{
        _integer: None, 
        _list: [
            NestedInteger{
                _integer: None, 
                _list: []
            }]
    }, 
    NestedInteger{
        _integer: None, 
        _list: [
            NestedInteger{
                _integer: 1, 
                _list: []
                }
            ]
        }, 
    NestedInteger{
        _integer: None, 
        _list: []
    }
]
"""
