class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        res = 0
        ans = float('inf')
        n = len(nums)
        while left <= right and right < n:
            res += nums[right]
            right += 1
            while res >= target:
                res -= nums[left]
                ans = min(ans, right-left)
                left += 1
        return ans if ans != float('inf') else 0
