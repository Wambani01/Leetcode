# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged = ListNode()
        temp = merged
        while list1 or list2:
            val1 = list1.val if list1 is not None else 101
            val2 = list2.val if list2 is not None else 101
            if val2 == val1:
                nodeval = val1
                for i in range(2):
                    NewNode = ListNode(nodeval)
                    temp.next = NewNode
                    temp = temp.next
                list1 = list1.next
                list2 = list2.next
                continue
            elif val2 < val1:
                nodeval = val2
                list2 = list2.next
            elif val2 > val1:
                nodeval = val1
                list1 = list1.next
            NewNode = ListNode(nodeval)
            temp.next = NewNode
            temp = temp.next
        
        merged = merged.next
        return merged
