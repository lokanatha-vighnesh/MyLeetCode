class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        d = {i:0 for i in set(nums)}
        for i in range(n-k+1):
            arr = nums[i:i+k]
            for j in arr:
                d[j] += 1
        
        val = -1
        for i, j in d.items():
            if j < 2:
                val = max(val, i)
            else:
                continue

        return val
