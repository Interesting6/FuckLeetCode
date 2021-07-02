# @before-stub-for-debug-begin
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

# def gen_children(node):
#     li = [[int(i) for i in node] for _ in range(8)]
#     for i in range(8):
#         li[i][i%4] += (i//4 * 2 - 1)
#         li[i] = [str(j%10) for j in li[i]]
#         li[i] = "".join(li[i])
#     return li


# class Solution:
#     def openLock(self, deadends: List[str], target: str) -> int:
#         root = "0000"
#         queue = []
#         used = set()
#         deadends = set(deadends)
#         queue.append(root)
#         used.add(root)
#         step = 0
#         while queue:
#             cur_size = len(queue)
#             for i in range(cur_size):
#                 node = queue.pop(0)
#                 if node == target:
#                     return step
#                 if node in deadends:
#                     continue
#                 children = gen_children(node)
#                 for sub_node in children:
#                     if sub_node not in used:
#                         queue.append(sub_node)
#                         used.add(sub_node)
#             step += 1
#         return -1

class Solution:
    def openLock(self, deadends, target):
        begin = "0000"
        deadends = set(deadends)
        if begin in deadends:
            return -1
        step = -1
        from collections import deque
        dq = deque([begin])
        vis = set([begin])
        def get_children(node: str) -> str:
            for i in range(4):
                for j in [-1, 1]:
                    nodet = list(node)
                    if nodet[i] == '0' and j == -1:
                        nodet[i] = '9'
                    elif nodet[i] == '9' and j == 1:
                        nodet[i] = '0'
                    else:
                        nodet[i] = str(int(nodet[i]) + j)
                    nodet = ''.join(nodet)
                    yield nodet

        while dq:
            sz = len(dq)
            step += 1
            for _ in range(sz):
                node = dq.popleft()
                if node == target:
                    return step
                for tp in get_children(node):
                    if (tp not in deadends) and (tp not in vis):
                        dq.append(tp)
                        vis.add(tp)
        return -1

""" 21-06-25每日一题
Accepted
48/48 cases passed (780 ms)
Your runtime beats 51.97 % of python3 submissions
Your memory usage beats 55.68 % of python3 submissions (16 MB)
"""

# deadends = ["0201","0101","0102","1212","2002"];target = "0202"
# deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]; target = "8888"
# deadends = ["0000"]; target = "8888"
# s = Solution().openLock(deadends, target)
# print(s)

# @lc code=end

