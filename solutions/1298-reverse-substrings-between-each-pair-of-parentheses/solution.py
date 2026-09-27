class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] != ')':
                stack.append(s[i])
            else:
                ans = []
                while stack:
                    val = stack.pop()
                    if val == '(':
                        break
                    ans.append(val)
                stack.extend(ans)

        return "".join(stack)
