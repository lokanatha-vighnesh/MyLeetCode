class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        string = []
        n = len(s)
        for i in range(n):
            for j in range(i,n+1):
                strr = s[i:j]
                if strr.count('1') == k:
                    string.append(strr)
        string.sort(key = lambda x: (len(x),x))
        return string[0] if string else ""
