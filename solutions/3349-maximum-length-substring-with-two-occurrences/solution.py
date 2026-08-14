class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        sets = set(s)
        
        ans = 0
        var = False
        for left in range(len(s)):
            dic = {}            
            for right in range(left,len(s)):
                if s[right] in dic:
                    dic[s[right]] += 1
                else:
                    dic[s[right]] = 1
                for i in dic.values():
                    if i == 2 or i == 1:
                        var = True
                        continue
                    else:
                        var = False
                        break
                if var:
                    ans = max(ans, right-left+1)
        return ans
