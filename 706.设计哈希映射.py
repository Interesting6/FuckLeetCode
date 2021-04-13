#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#

# @lc code=start
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1009
        self.map = [[] for _ in range(self.buckets)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        row, col = key // 1000, key % 1000
        if not self.map[row]:
            self.map[row] = [-1] * self.buckets
        self.map[row][col] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        row, col = key // 1000, key % 1000
        if not self.map[row]:
            return -1
        return self.map[row][col]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        row, col = key // 1000, key % 1000
        if self.map[row]:
            self.map[row][col] = -1
"""
分桶数一般取质数，这是因为经验上来说，质数个的分桶能让数据更加分散到各个桶中。下面的代码中把分桶数去了 1009，是因为 1009 是大于 1000 的第一个质数。

Accepted
36/36 cases passed (172 ms)
Your runtime beats 98.83 % of python3 submissions
Your memory usage beats 57.08 % of python3 submissions (18.1 MB)
"""


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

