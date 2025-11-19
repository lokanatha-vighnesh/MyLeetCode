class Solution(object):
    def findFinalValue(self, nums, original):
        variable = True
        i=0
        while i != len(nums):
            if nums[i] == original:
                original *= 2
                i=0
            else:
                i+=1
        return original
