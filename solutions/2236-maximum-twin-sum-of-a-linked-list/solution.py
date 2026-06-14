# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        duplicate = head
        count = 1
        while duplicate.next != None:
            duplicate = duplicate.next
            count += 1
        i=0
        dup2 = head
        while i < (count/2):
            dup2 = dup2.next
            i+=1
        arr1 = [0]*(count//2)
        arr2 = [0]*(count//2)
        j=0
        while head != None and dup2 != None:
            arr1[j] = head.val
            arr2[(count//2)-j-1] = dup2.val
            head = head.next
            dup2 = dup2.next
            j+=1
        ans = 0
        print(arr1, arr2)
        for i in range((count//2)):
            ans = max(ans, arr1[i]+arr2[i])
        return ans
