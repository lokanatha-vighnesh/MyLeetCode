class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        stack = []
        for i in range(n):
            val = s[i]
            if val == '(':
                stack.append(val)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(val)
        return len(stack)
