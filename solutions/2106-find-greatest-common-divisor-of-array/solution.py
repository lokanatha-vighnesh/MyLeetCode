class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small = float('inf')
        large = 0
        for i in range(len(nums)):
            if nums[i] > large:
                large = nums[i]
            if nums[i] < small:
                small = nums[i] 
        while small != 0:
            large, small = small, large%small
        return large
