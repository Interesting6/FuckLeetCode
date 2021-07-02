#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
"""关键点：如果左边分配好了节点个数，则根节点必然也固定了！
如，当左边有k个节点，根节点必然是k+1，右边必须放n-(k+1)个
    否者若根节点为k-1，则小于k-1还有k-2个，左边只能放下k-2，与左边有k个节点毛盾
    同理若根节点为k+2，则大于k+1的还有n-(k+2)个，右边只能放下n-(k+2)，与右边有n-(k+1)毛盾
"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1 # 无节点时，因为后面设计到乘法，故设为1
        dp[1] = 1
        for i in range(2, n+1): # 总共i个节点时
            for k in range(1, i+1): # k为根节点的标号
                dp[i] += dp[k-1]*dp[i-k] # 左边的节点数能构成的树数*右边节点数能构成的树数

        return dp[n]

s = Solution().numTrees(3)
print(s)
# @lc code=end

