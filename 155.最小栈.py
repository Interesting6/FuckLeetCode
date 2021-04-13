#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.aux_stack = [] # 栈顶维护最小元素


#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         if not self.aux_stack:
#             self.aux_stack.append(x)
#         else:
#             if x <= self.aux_stack[-1]:   
#                 self.aux_stack.append(x)
#             # 当添加的元素不是最小值时，不入栈

#     def pop(self) -> None:
#         x = self.stack.pop()
#         if x == self.aux_stack[-1]: 
#             self.aux_stack.pop()
#         return x
#         # pop栈顶元素时，前面的元素最小值也一定在辅助栈里，有点像动态规划

#     def top(self) -> int:
#         return self.stack[-1]

#     def getMin(self) -> int:
#         return self.aux_stack[-1]


"""21.03.18做"""
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.aux_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.aux_stack:
            self.aux_stack.append(val)
        else:
            if self.aux_stack[-1] >= val:
                self.aux_stack.append(val)

    def pop(self) -> None:
        if self.aux_stack[-1] == self.stack[-1]:
            self.stack.pop()
            self.aux_stack.pop()
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.aux_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

