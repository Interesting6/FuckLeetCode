#
# @lc app=leetcode.cn id=1239 lang=python3
#
# [1239] 串联字符串的最大长度
#

# @lc code=start 
# 2021-06-19每日一题，不会
from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        length = len(arr)
        masks = []
        for s in arr:
            mask = 0
            for ch in s:
                idx = ord(ch) - ord('a')
                if ( (mask>>idx) & 1 ): # mask已有ch，#! 说明s含有重复字母，无法构成可行解
                    mask = 0  # 这个时候就不会加入masks里了 #! pass掉
                    break
                mask |= ( 1<<idx ) # 将ch加入mask中，#& 易见每个ch只占mask中的一个位
            if (mask > 0): # 有效的mask，直接把含重复元素的pass掉
                masks.append(mask)
        
        ans = 0
        def backtrack(pos, mask):
            if pos == len(masks): # 最后只需对masks里的元素进行就行
                nonlocal ans
                ans = max(ans, bin(mask).count('1'))
                return
            if ((mask & masks[pos]) == 0): # mask与masks[pos]无公共元素，可以选第pos个数
                # 在pos位置，且选第pos个数
                backtrack(pos+1, mask | masks[pos]) #& 更新当前的mask为老mask和第pos数的mask的或
            # 上面if结束后，隐含的进行了回溯，回到了pos的位置，且不选第pos个数
            backtrack(pos+1, mask) # 不选第pos个数，不用更新mask
            # 即每个数都一定会有不选的时候。这时前面不选，后面选的情况就会发生。
            
        backtrack(0, 0) # 从第0个数开始，存在的字符为0
        return ans
"""
Accepted
85/85 cases passed (80 ms)
Your runtime beats 90.03 % of python3 submissions
Your memory usage beats 50.17 % of python3 submissions (15.1 MB)
"""
arr = ["un","iq","une"]
s = Solution().maxLength(arr)
print(s)

# @lc code=end

