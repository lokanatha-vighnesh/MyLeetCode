# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):

        x = ListNode(0)
        answer = x

        while l1 is not None and l2 is not None:
            if l1.val <= l2.val :
                answer.next = l1
                l1 = l1.next
            else:
                answer.next = l2
                l2 = l2.next
            answer = answer.next
        
        if l1 is not None:
            answer.next = l1
        elif l2 is not None:
            answer.next = l2

        return x.next


        
