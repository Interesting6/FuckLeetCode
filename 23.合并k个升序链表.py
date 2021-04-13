#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge2(link1, link2):
            dummy_head = ListNode(-10**4-1)
            cur = dummy_head
            while link1 and link2:
                if link1.val < link2.val:
                    cur.next = link1
                    link1 = link1.next
                else:
                    cur.next = link2
                    link2 = link2.next
                cur = cur.next
            if link1:
                cur.next = link1
            else:
                cur.next = link2
            return dummy_head.next
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        # 顺序合并：9%，总时间复杂度为k**2*n
        # res = ListNode(-10**4-1)
        # for i in range(n):
        #     res = merge2(res, lists[i])
        # return res.next
        # 分治合并：时间超44.45%，空间超96.89%，总时间复杂度为kn*logn，
        # 我咋感觉归并所需的次数跟上面顺序合并所需的合并次数一样多呀，可能是合并里面复杂度降低？
        def divideNDmerge(l, r):
            if l > r:
                return
            if l == r:
                return lists[l]
            mid = l + ((r-l)>>1)
            left = divideNDmerge(l, mid)
            right = divideNDmerge(mid+1, r)
            meg = merge2(left, right)
            return meg
        res = divideNDmerge(0, n-1)
        return res

# @lc code=end

