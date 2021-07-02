#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start
from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # length = len(people)
        # queue = [[0, 0] for _ in range(length)]
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = list()
        for person in people:
            ans[person[1]:person[1]] = [person] # 将people插入到k_j位置，
            # ans.insert(person[1], person) # 易懂点，但好像这样插入复杂度高？实验证明，确实上面的插入时间复杂度低
            # 这时h_j必然比之前的都小，所以插入到前面不会影响队列里已经拍好的人的k_j。
            # 而这时在插入位置前面有0-k_j-1，共k_j个人，满足people[1]的要求
        return ans

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
s = Solution().reconstructQueue(people)
print(s)

# import timeit
# import numpy as np

# def f1():
#     ans = []
#     for i in range(10000):
#         ans.insert(i//2, i)
#     return

# def f2():
#     ans = []
#     for i in range(10000):
#         ans[i//2:i//2] = [i]

# t1 = timeit.repeat(stmt=f1, number=1000, repeat=5)
# print(t1)
# print(np.mean(t1), np.std(t1))

# t2 = timeit.repeat(stmt=f2, number=1000, repeat=5)
# print(t2)
# print(np.mean(t2), np.std(t2))

# 结果为：
# 9.369280121987686
# 4.296615592902526

# @lc code=end

