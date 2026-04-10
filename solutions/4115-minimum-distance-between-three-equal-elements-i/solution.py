class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        val = float("inf")
        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    if i!=j and j!=k and k!=i and nums[i]==nums[j]==nums[k]:
                        val = min(val,abs(i-j)+abs(j-k)+abs(k-i))

        return val if val != float("inf") else -1
