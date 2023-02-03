# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        nodes = ListNode()
        temp = nodes
        remainder = 0
        while l1 or l2 or remainder:
            l2val = 0 if l2 is None else l2.val
            l1val = 0 if l1 is None else l1.val
            total = l1val + l2val + remainder
            nodeval = total % 10 if total > 9 else total
            remainder = total // 10 if total > 9 else 0
            NewNode = ListNode(nodeval, None)
            temp.next = NewNode
            temp = temp.next
            if l1 is None and l2 is None:
                remainder = 0
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        nodes = nodes.next
        return nodes
        
