class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        left = 0
        right = n-1
        ans = -1
        while left <= right:
            if colors[left] == colors[right]:
                right -= 1
            else:
                ans = max(ans,abs(left-right))
                left += 1
                right = n-1
        return ans
