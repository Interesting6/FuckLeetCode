#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if not self.queue1 and not self.queue2:
            self.queue1.append(x)
        elif not self.queue1 and self.queue2:
            self.queue2.append(x)
        elif self.queue1 and not self.queue2:
            self.queue1.append(x)
        # 必定有一个queue为空

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.queue1 and not self.queue2:
            n = len(self.queue1)
            while n > 1:
                self.queue2.append(self.queue1.pop(0))
                n -= 1
            return self.queue1.pop()
        elif not self.queue1 and self.queue2:
            n = len(self.queue2)
            while n > 1:
                self.queue1.append(self.queue2.pop(0))
                n -= 1
            return self.queue2.pop()
        # 将空的那个queue来存放先入的点


    def top(self) -> int:
        """
        Get the top element.
        """
        if self.queue1 and not self.queue2:
            return self.queue1[-1]
        elif not self.queue1 and self.queue2:
            return self.queue2[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.queue1 or self.queue2:
            return True
        else:
            return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

