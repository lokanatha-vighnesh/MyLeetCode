
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        d = [0] * 3
        for s in stones:
            d[s % 3] += 1
        
        if d[0] % 2 == 0:
            return d[1] >= 1 and d[2] >= 1
        return abs(d[1] - d[2]) > 2
