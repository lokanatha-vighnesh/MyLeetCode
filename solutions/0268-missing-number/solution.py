class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0]*(n+1)
        for i in nums:
            count[i] += 1
        print(nums, count)
        ans = 0
        for i in range(n+1):
            if count[i] == 0:
                ans = i

        return ans
