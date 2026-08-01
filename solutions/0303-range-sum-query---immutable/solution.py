class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def prefixsum(self,nums):
        for i in range(1,len(nums)):
            self.nums[i] += self.nums[i-1]
    def sumRange(self, left: int, right: int) -> int:
        s = 0
        for i in range(left,right+1):
            s += self.nums[i]

        return s
