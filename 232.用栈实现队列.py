#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.aux_stack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.aux_stack:
            return self.aux_stack.pop()
        while self.stack:
            self.aux_stack.append(self.stack.pop())
        return self.aux_stack.pop()



    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.aux_stack:
            return self.aux_stack[-1]
        else:
            return self.stack[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.stack or self.aux_stack: # 有一个不为空
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

