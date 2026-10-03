class Solution:
    def isValid(self,s):
        n = len(s)
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    return False
        return not stack
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = [-1]
        ans = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    v = stack.pop()
                    if stack:
                        prev = stack[-1]
                        ans = max(ans,i-prev)
                    else:
                        stack.append(i)
                else:
                    stack.append(i)

        return ans
