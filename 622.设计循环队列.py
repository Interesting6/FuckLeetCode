# @before-stub-for-debug-begin
from python3problem622 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 设计循环队列
#

# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.size = k # total capacity
        self.sp = 0 # start point
        self.ep = 0 # end point
        self.rp = 0 # relative position
        self.cs = 0 # current size


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.queue[self.ep] = value
        if self.ep == self.size-1:
            self.ep = 0
        else:
            self.ep += 1

        self.cs += 1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.queue[self.sp]
        if self.sp == self.size-1:
            self.sp = 0
        else:
            self.sp += 1
        self.cs -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.sp]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.ep-1]


    def isEmpty(self) -> bool:
        if self.cs == 0:
            return True
        else:
            return False


    def isFull(self) -> bool:
        if self.cs == self.size:
            return True
        else:
            return False



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end


def BFS(root, target) {
    queue = []  # 存储所有等候处理的节点
    step = 0    # 当前节点到根节点的步数/层数
    queue.append(root)
    # BFS
    while queue:
        step += 1
        cur_size = len(queue)
        for i in range(cur_size):
            cur_node = queue.pop(0)
            if cur_node == target: # 当前节点就是目标节点，返回此时距根节点的步长
                return step
            for node in cur_node.children:
                queue.append(node)
    
    return -1;          # 没找到从root到target的路径
}