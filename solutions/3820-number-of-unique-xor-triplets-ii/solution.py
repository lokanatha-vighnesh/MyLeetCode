class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        n = len(nums)
        d = set()
        for i in range(n):
            for j in range(i,n):
                d.add(nums[i] ^ nums[j])
        c = 0
        s = set()
        d = list(d)
        for i in range(len(nums)):
            for j in range(len(d)):
                s.add(nums[i]^d[j])

        return len(s)
