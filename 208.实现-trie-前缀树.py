# @before-stub-for-debug-begin
from python3problem208 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isEnd = False
        self.next = [None] * 26
        # 注意值在边上，而跟传统树不一样值在节点上


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for c in word:
            idx = ord(c) - 97
            if not node.next[idx]:
                node.next[idx] = Trie()
            node = node.next[idx]
        node.isEnd = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for c in word:
            idx = ord(c) - 97
            node = node.next[idx] # 根据边查找下一个节点
            if not node: # node为None时，叶子节点node不为None或False
                return False
        return node.isEnd # 最后一个节点是叶子节点


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for c in prefix:
            idx = ord(c) - 97
            node = node.next[idx]
            if not node:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

