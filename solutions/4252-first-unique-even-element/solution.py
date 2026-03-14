class Solution(object):
    def firstUniqueEven(self, nums):
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        for i in range(len(nums)):
            if nums[i] % 2 == 0 and count[nums[i]] == 1:
                return nums[i]


        return -1
