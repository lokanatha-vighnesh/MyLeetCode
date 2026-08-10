import math

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {0: False}
        def dp(n):
            if n in memo:
                return memo[n]
            k = 1
            while k * k <= n:
                if not dp(n-k*k):
                    memo[n] = True
                    return True
                k += 1
            memo[n] = False
            return False


        return dp(n)

        dp = [False]*(n+1)

        for i in range(1,n+1):
            k = 1
            while k*k <= n:
                if not dp[i-k*k]:
                    dp[i] = True
                    break
                k += 1

        
        return dp[n]


