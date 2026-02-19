class Solution(object):
    def countBinarySubstrings(self, s):
        ans = [1]
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                ans[len(ans)-1] += 1
            else:
                ans.append(1)
        result = 0
        for i in range(1,len(ans)):
            result += min(ans[i-1],ans[i])
        
        return result
