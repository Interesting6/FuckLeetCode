
#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start

class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DoubleList:
    def __init__(self):
        self.size = 0
        self.dummy_head = ListNode()
        self.dummy_tail = ListNode()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def add2Head(self, node): # 在开头增加一个节点
        node.next = self.dummy_head.next
        self.dummy_head.next.prev = node
        node.prev = self.dummy_head
        self.dummy_head.next = node
        self.size += 1

    def removeNode(self, node): # 删除中间一个节点
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def removeTail(self): # 删除末尾节点，并将其返回
        node = self.dummy_tail.prev
        self.removeNode(node)
        return node

    def move2Head(self, node): # 将节点移到头部
        self.removeNode(node) 
        # 单独写可能难以理解，为什么不用先找到node的位置，再删除
        # 这里删除相当于直接通过node本身前面接到后面，后面接到前面，而与链表无关的样子
        # 这样可行吗？关键node不一定就是从这个链表里取出的呀？
        # 因为在主类的添加操作都是直接在node上进行的，所以node也在随着改变，即node一定在链表里，所以这里直接操作node就行。
        # 这点很神奇！
        self.add2Head(node)

    def __str__(self):
        # 用于调试
        li = []
        cur = self.dummy_head.next
        while cur != self.dummy_tail :
            li.append((cur.key, cur.val))
            cur = cur.next
        return str(li)

"""
首先使用哈希表进行定位，找出缓存项在双向链表中的位置，
"""
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dbList = DoubleList()

    def get(self, key: int) -> int:
        # print("get", key, self.dbList)
        if key not in self.cache: # 不在后台
            return -1
        else: 
            node = self.cache[key]
            self.dbList.move2Head(node)
            return node.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache: # 不在后台，创建一个新的节点
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self.dbList.add2Head(new_node) # 将该节点加到链表头部，因为将其加到链表里面了，所以node都在变？而不是纯粹的一个节点？
            if self.dbList.size > self.capacity: # 缓存的数目多了，删除最尾端的
                removed = self.dbList.removeTail()
                self.cache.pop(removed.key) # 同时把cache的最尾端的那个映射也删掉
        else: # 在后台，更新缓存，并移到最前面
            node = self.cache[key]
            node.val = value # 更新val的值
            self.dbList.move2Head(node) # 移到前面去
        # print("put", (key, value), self.dbList)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

