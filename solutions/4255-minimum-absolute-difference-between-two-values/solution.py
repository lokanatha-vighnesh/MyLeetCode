class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(n):
                if nums[i] == 1 and nums[j] == 2:
                    res.append(abs(i-j))
        
        return min(res) if res else -1
