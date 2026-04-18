class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n = len(nums)
        ans = []
        for i in range(n):
            if nums[i] == target:
                ans.append(abs(i-start))


        return min(ans)
