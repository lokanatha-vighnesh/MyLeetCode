class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        d = {}
        for i in range(n):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        string = ""
        middle = ""
        arr = sorted(list(d.keys()))
        for i in range(len(arr)):
            string += arr[i]*(d[arr[i]]//2)
            if d[arr[i]] %  2 == 1:
                middle += arr[i]
        return string + middle + string[::-1]
