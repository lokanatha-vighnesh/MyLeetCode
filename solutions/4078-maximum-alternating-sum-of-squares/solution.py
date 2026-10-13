class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted(nums,key = lambda x:abs(x))
        n = len(nums)
        mid = n // 2
        ans = 0
        for i in range(n):
            if i < mid:
                ans -= nums[i]**2
            else:
                ans += nums[i]**2
        return ans
