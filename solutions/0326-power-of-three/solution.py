class Solution(object):
    def isPowerOfThree(self, n):
        return n in [3**i for i in range(30)]
        
