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

        return 
# @lc code=end

