class Solution(object):
    def repeatedNTimes(self, nums):
        not_repeated = []
        n = len(nums)
        for i in range(n):
            if nums[i] not in not_repeated:
                not_repeated.append(nums[i])
            else:
                return nums[i]

        
