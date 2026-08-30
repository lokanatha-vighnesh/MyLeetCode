class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mi, ma = 0, 0
        n = len(nums)
        for i in range(1,n):
            if nums[i] > nums[ma]:
                ma = i
            if nums[i] < nums[mi]:
                mi = i
        
        return min(max(mi+1,ma+1),max(n-ma, n-mi),n-ma+mi+1,n-mi+ma+1)
