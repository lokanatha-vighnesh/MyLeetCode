class Solution:
    def number(self,num):
        num = str(num)
        s = 0
        for i in range(len(num)):
            s += int(num[i])
        return s

    def minElement(self, nums: List[int]) -> int:
        min_ele = float('inf')
        for i in nums:
            min_ele = min(min_ele, self.number(i))
        
        return min_ele
