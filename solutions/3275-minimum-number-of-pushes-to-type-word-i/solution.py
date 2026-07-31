class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <= 8:
            return n
        if n > 8 and n <= 16:
            return 8 + 2*(n-8)
        if n > 16 and n <= 24:
            return 8 + 16 + 3*(n-16)
        if n > 24:
            return 8 + 16 + 24 + 4*(n-24)
