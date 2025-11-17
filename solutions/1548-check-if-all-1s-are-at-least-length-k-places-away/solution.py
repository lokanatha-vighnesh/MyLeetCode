class Solution(object):
    def kLengthApart(self, nums, k):
        num = []
        for i,j in enumerate(nums):
            if j == 1:
                num.append(i)
            else:
                continue
        for i in range(len(num)-1):
            if num[i+1]-num[i] <= k:
                return False
        return True
                

        
