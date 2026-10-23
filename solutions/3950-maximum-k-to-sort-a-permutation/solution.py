class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        val = None
        for i in range(n):
            if i == nums[i]:
                continue
            else:
                if val is None:
                    val = nums[i]
                val &= nums[i]
        return val if val else 0
