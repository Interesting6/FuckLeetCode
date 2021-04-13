#
# @lc app=leetcode.cn id=781 lang=python3
#
# [781] 森林中的兔子
#

# @lc code=start
# 当兔子回答x时，最多允许x+1只同色的兔子同时回答x。
# 统计数组中回答为x的兔子个数为n
# 则这n只兔子中，每x+1的兔子为一个小组，该小组里的兔子回答的都是x
# 共 ceil(n / (x+1)) 个小组，且每个小组至少x+1只兔子
# 那么当n不整除x+1时，最后一个小组不到x+1只兔子，
# 但因为该小组的兔子回答的是x，表明还有至少x只兔子跟他同色，只是没有参与回答。
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        if not answers:
            return 0
        from collections import Counter
        cnt = Counter(answers)
        res = 0
        for x,n in cnt.items():
            ng = math.ceil(n / (x+1))
            res += ng * (x+1)
        return res
        
# @lc code=end

