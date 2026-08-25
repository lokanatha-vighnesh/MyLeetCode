class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)
        values = set()
        for i in range(n):
            val = nums[i]
            mul = nums[i] // k
            if val == mul*k:
                values.add(val)
        i = 1
        while k*i in values:
            i += 1

        return k*i 
