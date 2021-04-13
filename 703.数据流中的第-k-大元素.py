# @before-stub-for-debug-begin
from python3problem703 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#

# @lc code=start
"""直接调库，维持一个大小为k的最小堆，则堆顶元素即为第k大"""
# import heapq
# class KthLargest:
#     def __init__(self, k, nums):
#         self.heap = []
#         self.k = k
#         for num in nums:
#             heapq.heappush(self.heap, num)
#             if len(self.heap) > k: # 如果堆里元素个数大于k
#                 heapq.heappop(self.heap) # 将堆顶元素(第k+1大的元素推出)
#                 # 维持了堆顶元素是最小的元素，即后面k-1个元素都比其大，即
#                 # 即堆顶元素为第k大元素。

#     def add(self, val):
#         heapq.heappush(self.heap, val)
#         if len(self.heap) > self.k:
#             heapq.heappop(self.heap)
#         return self.heap[0]



"""手撸最小堆"""
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = myHeap()
        for i in nums:
            self.heap.insert(i)
            if len(self.heap) > k:
                self.heap.remove()

    def add(self, val: int) -> int:
        self.heap.insert(val)
        if len(self.heap) > self.k:
            self.heap.remove()
        return self.heap.heap[0]

class myHeap:
    def __init__(self, desc=False):
        self.heap = []
        self.desc = desc
    
    @property
    def size(self):
        return len(self.heap)
    
    def __len__(self):
        return self.size

    def insert(self, val):
        self.heap.append(val) # 加到堆底
        self.swim(self.size-1)  # 将刚加到堆底的元素上浮

    def remove(self):
        t = self.heap[0]
        self.heap[0] = self.heap.pop() # 将堆底元素取出删除，并放入堆顶
        self.sink(0)
        return t # 返回堆顶元素

    def sink(self, i):
        # 下沉第i个元素
        while self._left(i) < self.size: # 有左节点
            smallest = i
            left = self._left(i)
            right = self._right(i)
            if self._less(left, smallest): # 左子节点更小
                smallest = left  # 将最小的设为左子节点
            if right < self.size and self._less(right, smallest):
                # 右子节点存在，且右子节点更小，则将更小的那个设为最小的
                smallest = right
            if smallest == i:
                break # 当前节点比子节点都小
            else:
                self._swap(smallest, i) # 当前节点与最小那个子节点交换
                i = smallest # i进入到下层

    def swim(self, i):
        # 上浮第i个元素
        while i >= 0 and self._parent(i) >= 0:
            father = self._parent(i)
            if self._less(i, father):
                self._swap(i, father)
                i = father
            else:
                break

    def _parent(self, i):
        # 第i个节点的父节点索引
        return (i-1) // 2
    def _left(self, i):
        return i * 2 + 1
    def _right(self, i):
        return i * 2 + 2
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def _less(self, i, j):
        return self.heap[i] < self.heap[j]
    
"""
Accepted
10/10 cases passed (292 ms)
Your runtime beats 24.03 % of python3 submissions
Your memory usage beats 43.86 % of python3 submissions (18.5 MB)
"""

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(i, nums)
# param_1 = obj.add(val)
# @lc code=end

