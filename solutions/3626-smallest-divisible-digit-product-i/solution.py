class Solution:
    def product(self,s):
        product = 1
        for i in s:
            product *= int(i)
        return product
    def smallestNumber(self, n: int, t: int) -> int:
        s = str(n)
        i = n
        while self.product(s) % t != 0:
            s = str(int(s)+1)

        return int(s) 
