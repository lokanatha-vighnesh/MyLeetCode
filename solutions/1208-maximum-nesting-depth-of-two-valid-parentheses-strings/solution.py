class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        layer = 0
        n = len(seq)
        ans = [0]*n
        for i in range(n):
            if seq[i] == '(':
                layer += 1
                ans[i] = 0 if layer % 2 == 1 else 1
            if seq[i] == ')':
                ans[i] = 0 if layer % 2 == 1 else 1
                layer -= 1
            
        
        return ans
