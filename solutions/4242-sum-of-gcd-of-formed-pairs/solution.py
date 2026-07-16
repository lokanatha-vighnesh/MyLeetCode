import math

class Solution(object):
            
    def gcdSum(self, nums):
        n = len(nums)
        prefixGcd = [0]*n
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        mx = 0
        for i in range(n):
            if nums[i] > mx:
                mx = nums[i]
            prefixGcd[i] = gcd(nums[i],mx)

        prefixGcd.sort()
        ans = 0
        for i in range(n//2):
            ans += gcd(prefixGcd[i],prefixGcd[-(i+1)])

        return ans
