class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        a,b = [0]*26,[0]*26
        for i in range(len(s)):
            a[ord(s[i])-ord('a')] += 1
            b[ord(t[i])-ord('a')] += 1

        return a == b
