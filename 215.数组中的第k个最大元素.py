#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr, s, e):
            pivot = arr[e]
            i = s
            for j in range(s, e):
                if arr[j] >= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i], arr[e] = arr[e], arr[i]
            return i

        def qsort(arr, s, e):
            if s < e:
                m = partition(arr, s, e)
                qsort(arr, s, m-1)
                qsort(arr, m+1, e)
        n = len(nums)
        qsort(nums, 0, n-1)
        # print(nums)
        return nums[k-1]
"""
Accepted
32/32 cases passed (5728 ms)
Your runtime beats 5 % of python3 submissions
Your memory usage beats 5 % of python3 submissions (20.9 MB)
"""

# @lc code=end

