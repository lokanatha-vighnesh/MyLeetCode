class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        mid1 = nums[n//2]
        mid2 = nums[n//2+1] if n//2 > 1 else mid1
        count1, count2 = 0, 0
        for i in nums:
            count1 += abs(mid1-i)
            count2 += abs(mid2-i)

        return min(count1,count2)
