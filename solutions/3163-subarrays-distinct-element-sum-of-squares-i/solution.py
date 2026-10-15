class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        for i in range(2,n+1):
            for j in range(n-i+1):
                ans += (len(set(nums[j:j+i])))**2

        return ans
