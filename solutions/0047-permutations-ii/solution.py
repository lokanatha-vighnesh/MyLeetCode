class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 1:
            return [nums]
        ans = []
        for i in range(n):

            head = nums[i]

            rem = nums[:i]+nums[i+1:]

            for perm in self.permuteUnique(rem):
                l = [head]+perm
                if l not in ans:
                    ans.append(l)


        return ans
