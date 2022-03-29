# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        l=[]
        while head is not None:
            l.append(str(head.val))
            head=head.next
            
        return int(''.join(l),2)
        """
        :type head: ListNode
        :rtype: int
        """
        
