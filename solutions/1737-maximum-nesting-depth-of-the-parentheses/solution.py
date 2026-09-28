class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        n = len(s)
        ans = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(s)
            elif s[i] == ')':
                stack.pop()
            else:
                continue
            ans = max(ans,len(stack))
        return ans
