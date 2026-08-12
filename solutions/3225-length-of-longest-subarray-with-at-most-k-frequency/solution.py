class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d = {i:0 for i in set(nums)}
        n = len(nums)
        left = 0
        ans = 0
        for right in range(n):
            d[nums[right]] += 1
            while d[nums[right]] > k and left <= right:
                d[nums[left]] -= 1
                left += 1
                ans = max(ans, right-left+1)
            
        ans = max(ans, right-left+1)

        return ans
