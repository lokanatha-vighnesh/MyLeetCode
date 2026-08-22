class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s = str(n)
        sx = str(x)
        for i in range(len(s)):
            if i == 0 and s[i] == sx:
                return False
            if s[i] == sx:
                return True

        return False
