class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        if n % 2 == 1:
            return False
        for i in range(n):
            e = s[i]
            if e in ['(','[','{']:
                stack.append(e)
            else:
                p = stack[-1] if stack else '.'
                if (e == ')' and p == '(') or (e == ']' and p == '[') or (e == '}' and p == '{'):
                    stack.pop()
                else:
                    return False
        return not stack
