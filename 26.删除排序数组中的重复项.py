#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        if n < 2:
            return n
        i = 1 # 维护已处理好的序列
        j = 1 # 遍历
        while j < n:
            if nums[j] > nums[i-1]: # i-1是维护好的升序序列中最后一个(最大的)，
                # 若后面还出现比其大，则加入维护序列中
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            else: # 不比维护序列中最大的大，即在该序列里肯定有重复，跳过即可
                pass
            j += 1
        return i


# @lc code=end

