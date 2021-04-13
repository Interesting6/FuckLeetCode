# @before-stub-for-debug-begin
from python3problem752 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def gen_children(node):
    li = [[int(i) for i in node] for _ in range(8)]
    for i in range(8):
        li[i][i%4] += (i//4 * 2 - 1)
        li[i] = [str(j%10) for j in li[i]]
        li[i] = "".join(li[i])
    return li


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        root = "0000"
        queue = []
        used = set()
        deadends = set(deadends)
        queue.append(root)
        used.add(root)
        step = 0
        while queue:
            cur_size = len(queue)
            for i in range(cur_size):
                node = queue.pop(0)
                if node == target:
                    return step
                if node in deadends:
                    continue
                children = gen_children(node)
                for sub_node in children:
                    if sub_node not in used:
                        queue.append(sub_node)
                        used.add(sub_node)
            step += 1
        return -1

# @lc code=end

