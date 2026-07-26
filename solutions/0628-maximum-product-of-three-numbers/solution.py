class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """ n = len(nums)
        ans = float('-inf')
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if ans < nums[i]*nums[j]*nums[k]:
                        ans = nums[i]*nums[j]*nums[k]


        return ans """

        nums = sorted(nums)
        v1 = nums[0]*nums[1]*nums[-1]
        v2 = nums[-1]*nums[-2]*nums[-3]
        return max(v1,v2)
