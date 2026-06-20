class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        num = 0
        ans = 0
        for i in gain:
            num = num+i
            ans = max(ans,num)
        return ans
