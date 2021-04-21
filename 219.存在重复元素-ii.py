#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        n = len(nums)
        l = 0
        r = l
        st = set()
        while r <= l+k and r<n:
            if nums[r] not in st:
                st.add(nums[r])
            else:
                return True
            r += 1
        r -= 1
        while l < n-1:
            st.remove(nums[l])
            l += 1
            r += 1
            if r < n:
                if nums[r] not in st:
                    st.add(nums[r])
                else:
                    return True
            else:
                return False
        return False

# nums = [1,0,1,1]
# n = 1
# s = Solution().containsNearbyDuplicate(nums, n)
# print(s)
"""
Accepted
23/23 cases passed (44 ms)
Your runtime beats 82.1 % of python3 submissions
Your memory usage beats 85.91 % of python3 submissions (19.2 MB)
"""
# @lc code=end

