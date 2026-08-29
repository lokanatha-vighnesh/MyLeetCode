class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        def dp(idx):
            if idx == n-1:
                return True
            if nums[idx] == 0:
                return False
            if idx in memo:
                return memo[idx]
            if idx+nums[idx] >= n-1:
                memo[idx] = True
                return True
            
            for i in range(nums[idx]):
                
                if dp(idx+i+1):
                    memo[idx+i+1] = True
                    return True
            memo[idx] = False
            return False

        return dp(0)
