class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        
        ans = 0
        val = 1000
        while val-1 < n:
            ans += n-(val-1)
            val *= 1000

        return ans
