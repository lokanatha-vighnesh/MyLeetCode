class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        total = 0
        val = 0
        for i in range(n):
            if nums[i] != 0:
                total ^= nums[i]
            else:
                val += 1
        if val == n:
            return 0
        if total == 0:
            return n-1
        return n
