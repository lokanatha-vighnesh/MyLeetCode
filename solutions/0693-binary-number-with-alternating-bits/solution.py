class Solution(object):
    def hasAlternatingBits(self, n):
        dn = n
        s = ""
        while dn > 0:
            if dn % 2 == 0:
                s = '0' + s
            else:
                s = '1' + s
            dn //= 2
        
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                continue
            else:
                return False
        return True

        
