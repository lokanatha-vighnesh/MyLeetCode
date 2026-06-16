class Solution:
    def remove(self,s):
        return s[:-1]
    def duplicate(self,s):
        return s+s
    def reverse(self,s):
        return s[::-1]
    def processStr(self, s: str) -> str:
        ans = ""
        if s == "":
            return s
        for i in s:
            if i == '*':
                ans = self.remove(ans)
            elif i == '#':
                ans = self.duplicate(ans)
            elif i == '%':
                ans = self.reverse(ans)
            else:
                ans = ans+i
        return ans
