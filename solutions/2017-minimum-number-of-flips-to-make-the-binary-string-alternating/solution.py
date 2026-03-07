class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s  
        
        target1 = ""
        target2 = ""
        for i in range(len(s)):
            target1 += "1" if i % 2 == 0 else "0"
            target2 += "0" if i % 2 == 0 else "1"
            
        ans = float('inf')
        diff1 = 0
        diff2 = 0
        
        for i in range(len(s)):
            if s[i] != target1[i]: diff1 += 1
            if s[i] != target2[i]: diff2 += 1
            
            if i >= n:
                #sliding window but recalculates the values
                if s[i - n] != target1[i - n]: diff1 -= 1
                if s[i - n] != target2[i - n]: diff2 -= 1
            
            if i >= n - 1:
                ans = min(ans, diff1, diff2)
                
        return ans
