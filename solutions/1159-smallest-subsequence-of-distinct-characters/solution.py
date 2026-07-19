class Solution(object):
    def smallestSubsequence(self, s):
        n = len(s)
        string = [s[0]]
        for i in range(1,n):
            char = s[i]
            if char in string:
                continue
            while (string) and (char < string[-1]) and (string[-1] in s[i+1:]):
                string = string[:-1]
            
            string.append(char)
            
        return "".join(string)
