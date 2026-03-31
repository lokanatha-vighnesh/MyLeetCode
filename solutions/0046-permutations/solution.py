class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 1:
            return [nums]
        all_perm = []
        for i in range(n):

            head = nums[i]

            rem = nums[:i]+nums[i+1:]

            for perm in self.permute(rem):
                all_perm.append([head]+perm)

        return all_perm

