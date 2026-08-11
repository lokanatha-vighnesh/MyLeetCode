class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        idx = 0
        total = nums[0]
        for i in range(1,n):
            if nums[i] == nums[i-1] + 1:
                total += nums[i]
            else:
                idx = i
                break
        while total in nums:
            total += 1

        return total
