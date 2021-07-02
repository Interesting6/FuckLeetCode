#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
from typing import List
# 若最大值在左侧则重新查找的方法超时

# 2021-04-21 上次看的答案没做
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        import heapq
        hq = []
        res = []
        for i in range(k):
            heapq.heappush(hq, (-nums[i], i))
        res.append(-hq[0][0]) # 堆顶元素即为最大值
        for i in range(k, n):
            while hq and hq[0][1] <= i-k: # 当滑窗里最大值的位置在滑窗外时，这里得用while，因为当最大值不是在边界的时候就没有被pop，需要被后续pop出来
                heapq.heappop(hq) # 把该元素剔除
            heapq.heappush(hq, (-nums[i], i)) # 加入i位置的元素
            res.append(-hq[0][0])
        return res

""" 第二次刷这个做出来了，堆的方式时间复杂度是nlogn的
如 [1,3,-1]时，堆为[3,1,-1]；[3,-1,-3]时，堆为[3,1,-1,-3]；
[-1,-3,5]时，堆先pop出3和1(这里体现出了while的作用)，然后再加入5。
Accepted
61/61 cases passed (772 ms)
Your runtime beats 26.62 % of python3 submissions
Your memory usage beats 12.51 % of python3 submissions (38.3 MB)
"""

"单调栈的方式"
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        from collections import deque
        stack = deque([])
        res = []
        for i in range(k): 
            while stack and stack[-1][0] < nums[i]:
                stack.pop()
            stack.append((nums[i], i))
        # 单调递减双端队列，队列首为最大值
        res.append(stack[0][0])
        for i in range(k, n):
            while stack and stack[0][1] <= i-k: # 队首的最大值已经不在窗口中
                stack.popleft()  # 删掉
            while stack and stack[-1][0] < nums[i]: # 维护队列单调递减
                stack.pop() # 比当前值小的都删掉，因为往后的窗口的最大值肯定不会是那些比当前值小的元素。
            stack.append((nums[i], i))
            res.append(stack[0][0])
        return res

"""
Accepted
61/61 cases passed (500 ms)
Your runtime beats 58.02 % of python3 submissions
Your memory usage beats 23.39 % of python3 submissions (28.3 MB)
"""

# nums = [1,3,-1,-3,5,3,6,7]; k = 3
# nums = [1]; k = 1
# nums = [1,-1]; k = 1
# nums = [9,11]; k = 2
# nums = [4, -2]; k = 2
# s = Solution().maxSlidingWindow(nums, k)
# print(s)
# @lc code=end

