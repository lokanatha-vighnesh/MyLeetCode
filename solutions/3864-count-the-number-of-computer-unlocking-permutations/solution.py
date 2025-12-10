class Solution(object):
    def factorial(Self,num):
        if num == 0 or num == 1:
            return num
        return num * factorial(num-1)
    def countPermutations(self, complexity):
        n = len(complexity)

        mod = (10**9) + 7

        count = 0
        if n <= 1:
            return n
        
        if max(complexity) == complexity[0]:
            return 0
        

        i = 1
        while i <= n-1:
            if complexity[0] < complexity[i]:
                count += 1
            else:
                return 0

            i += 1
        
        return (self.factorial(count)) % mod
