from collections import Counter
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        mid = ""
        half = Counter()

        for ch, cnt in freq.items():
            if cnt % 2:
                mid = ch
            half[ch] = cnt // 2

        m = sum(half.values())

        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i

        total_perm = fact[m]
        for cnt in half.values():
            total_perm //= fact[cnt]

        if k > total_perm:
            return ""

        chars = sorted(half.keys())
        first_half = []
        remaining = m
        current_perm = total_perm

        while remaining > 0:
            for ch in chars:
                if half[ch] == 0:
                    continue

                next_perm = current_perm * half[ch] // remaining

                if k > next_perm:
                    k -= next_perm
                else:
                    first_half.append(ch)
                    current_perm = next_perm
                    half[ch] -= 1
                    remaining -= 1
                    break

        first = "".join(first_half)
        return first + mid + first[::-1]
