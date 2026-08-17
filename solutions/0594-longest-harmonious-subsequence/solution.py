class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = Counter(nums)
        val = 0
        for i in d:
            if i-1 in d:
                val = max(val, d[i]+d[i-1])

        return val
