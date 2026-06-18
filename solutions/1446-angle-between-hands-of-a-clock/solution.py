class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ans = abs((minutes*5.5)-30*(hour%12))
        return min(ans,360-ans)

