#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start

# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         if not T:
#             return []
#         stack = []  # 递减栈
#         num = len(T)
#         res = [0] * num
#         for i in range(num):
#             while stack: # 栈里有元素
#                 if stack[-1][1] < T[i]: # 当前栈顶元素比当前元素小，则说明有增值出现
#                     little = stack.pop()
#                     res[little[0]] = i - little[0] # 得到该增值的步数
#                 else: # 栈顶元素比当前元素还大，说明没有增值出现，直接加入栈中
#                     stack.append((i, T[i]))
#                     break # 此时栈里一定有元素，不会执行下面的if语句进行重新添加
#             if not stack: # 栈里无元素了两种情况：1、一开始的stack空需要添加；2、当前元素比栈顶元素都大，上面的while导致栈为空
#                 stack.append((i, T[i]))
#         return res


class Solution:
    def dailyTemperatures(self, T):
        desc_stack = []
        res = [0] * len(T)
        for i, t in enumerate(T):
            if not desc_stack or desc_stack[-1][1] >= t:
                desc_stack.append((i, t))
            else:
                while desc_stack and desc_stack[-1][1] < t:
                    pre_i, pre_t = desc_stack.pop()
                    res[pre_i] = i - pre_i
                desc_stack.append((i, t))
        return res


# @lc code=end

