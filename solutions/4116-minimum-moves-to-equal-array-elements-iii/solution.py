class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        val = 0
        for i in nums:
            val += m-i
        return val
