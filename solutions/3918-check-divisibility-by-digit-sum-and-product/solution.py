class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)
        digit_sum = 0
        digit_product = 1
        for i in s:
            digit_sum += int(i)
            digit_product *= int(i)
        if n % (digit_sum + digit_product) == 0:
            return True
        else:
            return False
