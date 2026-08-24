class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        majority = n//2
        c = Counter(nums)
        ans = 0
        for i,j in c.items():
            if j > majority:
                ans = i

        return ans
