#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#

# @lc code=start

# class MyHashSet():
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.set = []

#     def add(self, key: int) -> None:
#         if key not in self.set:
#             self.set.append(key)

#     def remove(self, key: int) -> None:
#         if key in self.set:
#             self.set.remove(key)

#     def contains(self, key: int) -> bool:
#         """
#         Returns true if this set contains the specified element
#         """
#         return key in self.set

# 分桶数组法
class MyHashSet:
    """ 先对 key 进行 key / 32，确定当前 key 所在桶的位置（大概位置）
        再对 key 进行 key % 32，确定当前 key 所在桶中的哪一位（精确位置）
    """
    def __init__(self):
        self.set = [0 for _ in range(40000)] 
        # 不存在则为0；存在则不为0，一个整数表示为二进制形式，
        # 只有一个1其他都为0，表示这个整数能代表多个数

    def set_val(self, key, val):
        bucketIdx = key // 32
        bitIdx = key % 32
        if val:
            u = self.set[bucketIdx] | (1 << bitIdx)
            self.set[bucketIdx] = u
        else:
            u = self.set[bucketIdx] & ~(1 << bitIdx) # ~别写成-
            self.set[bucketIdx] = u

    def get_val(self, key):
        bucketIdx = key // 32
        bitIdx = key % 32
        u = (self.set[bucketIdx] >> bitIdx) & 1
        return u

    def add(self, key):
        self.set_val(key, 1)

    def remove(self, key):
        self.set_val(key, 0)

    def contains(self, key):
        u = self.get_val(key)
        return u == 1


# class MyHashSet:
#     """
#         第一个维度用于计算 hash 分桶，第二个维度寻找 key 存放具体的位置。
#         第二个维度的数组只有当需要构建时才会产生，这样可以节省内存。
#     """
#     def __init__(self):
#         self.buckets = 1000
#         self.itemsPerBucket = 1001
#         self.table = [[] for _ in range(self.buckets)]

#     def hash(self, key):
#         return key % self.buckets

#     def pos(self, key):
#         return key // self.buckets

#     def add(self, key):
#         hash_key = self.hash(key)
#         if not self.table[hash_key]: # 当前元素不在集合内
#             self.table[hash_key] = [0] * self.itemsPerBucket
#         self.table[hash_key][self.pos(key)] = 1

#     def remove(self, key):
#         hash_key = self.hash(key)
#         if self.table[hash_key]:  # 当前元素在集合内？
#             self.table[hash_key][self.pos(key)] = 0
        
#     def contains(self, key): # 返回当前元素在hash分桶的第二个集合内
#         hash_key = self.hash(key)
#         return (self.table[hash_key]!=[]) and (self.table[hash_key][self.pos(key)] == 1)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

