class Solution(object):
    def maxArea(self, height):
        n = len(height)
        left = 0
        right = n-1
        ans = 0
        """for i in range(n):
            for j in range(n):
                if i!=j :
                    ans = max(ans,min(height[i],height[j])*(j-i))"""
        while left < right:
            ans = max(ans,min(height[left],height[right])*(right-left))
            if height[left] < height[right]:
                left+=1
            else:
                right -= 1
        return ans


        
