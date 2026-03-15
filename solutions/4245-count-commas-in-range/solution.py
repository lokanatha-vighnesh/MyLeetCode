class Solution:
    def countCommas(self, n: int) -> int:
        length = len(str(n))
        if length < 4:
            return 0
        else:
            count = 0
            while n > 999:
                count += (n-999)
                n //= 1000

        return count
