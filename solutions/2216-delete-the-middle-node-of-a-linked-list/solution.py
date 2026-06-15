# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        count = 0
        while p != None:
            count += 1
            p = p.next
        if count == 1:
            return None
        mid = count//2 
        p2 = head
        i = 0
        while i < mid-1:
            p2 = p2.next
            i += 1
        p2.next = p2.next.next

        return head
