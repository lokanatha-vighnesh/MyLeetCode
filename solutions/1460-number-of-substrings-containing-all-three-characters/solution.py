class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc = {
               'a':0,
               'b':0,
               'c':0
               }
        n = len(s)
        count = 0
        i = 0
        for j in range(n):
            abc[s[j]] += 1
            while abc['a'] > 0 and abc['b'] > 0 and abc['c'] > 0:
                count += n-j
                abc[s[i]] -= 1
                i += 1
                
        return count
