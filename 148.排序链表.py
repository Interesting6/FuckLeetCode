#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        
        # 找到头结点和尾结点
        pHead = head
        pTail = head
        while pTail.next:
            pTail = pTail.next
        
        def merge_sort(start, end):
            if start == end: # 只有一个节点时
                return start 
            if start.next == end: # 剩余两个节点时
                if start.val < end.val:
                    return start
                else:
                    start.next = None
                    end.next = start
                    return end
            
            # 找到中间节点
            sp = start
            fp = start
            while fp != end:
                fp = fp.next
                sp = sp.next
                if fp != end:
                    fp = fp.next
            
            
            p2Head = sp.next # 右边链表的头结点
            # 断开两个子链表
            sp.next = None # 别忘了先断开，且需先对右边进行归并排序，
            # 否者若在断开之前就先对左边进行排序，则会使得右边的也加入了排序。
            Link2 = merge_sort(p2Head, end) # 对右边链表进行排序
            Link1 = merge_sort(start, sp) # 对左边链表排序

            # 归并
            dummy_head = ListNode(-1)
            cur = dummy_head
            p1 = Link1
            p2 = Link2
            while p1 and p2:
                if p1.val < p2.val:
                    cur.next = p1
                    p1 = p1.next
                else:
                    cur.next = p2
                    p2 = p2.next
                cur = cur.next
            if p1:
                cur.next = p1
            else:
                cur.next = p2
            return dummy_head.next

        res = merge_sort(pHead, pTail)
        return res

"""
Accepted
28/28 cases passed (464 ms)
Your runtime beats 36.33 % of python3 submissions
Your memory usage beats 47.4 % of python3 submissions (30 MB)
"""
        
# @lc code=end

