# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        lis = []
        while head != None:
            lis.append(head.val)
            head = head.next
        n = len(lis)
        index = []
        for i in range(1,n-1):
            if lis[i] < lis[i-1] and lis[i] < lis[i+1]:
                index.append(i)
            if lis[i] > lis[i-1] and lis[i] > lis[i+1]:
                index.append(i)
        l = len(index)
        if len(index) < 2:
            return [-1,-1]
        min_val = float('inf')
        for i in range(1,l):
            min_val = min(min_val,index[i]-index[i-1])

        max_val = max(index)-min(index)

        return [min_val,max_val]
