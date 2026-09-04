class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ans = -1
        n = len(nums)
        prefix = [nums[0]]*n
        suffix = [nums[-1]]*n
        for i in range(1,n):
            prefix[i] = max(nums[i],prefix[i-1])
            suffix[n-i-1] = min(suffix[n-i], nums[n-i-1])
        for i in range(n):
            val = prefix[i]-suffix[i]
            if val <= k:
                ans = i if ans == -1 else min(ans, i)


        return ans
        
