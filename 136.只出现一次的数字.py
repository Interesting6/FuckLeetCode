#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        st = set()
        for i in nums:
            if i in st:
                st.remove(i)
            else:
                st.add(i)
        return st.pop()
""" hash表的方法。还可以用位运算，其关键为亦或满足交换律！！！
Accepted
61/61 cases passed (48 ms)
Your runtime beats 77.91 % of python3 submissions
Your memory usage beats 79.29 % of python3 submissions (16.5 MB)
"""

# @lc code=end

