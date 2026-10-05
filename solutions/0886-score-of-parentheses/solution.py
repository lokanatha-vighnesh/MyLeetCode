class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = len(s)
        ans = 0
        depth = 0
        stack = []
        var = True
        for i in range(n):
            if s[i] == '(':
                var = True
                depth += 1
                stack.append(s[i])
            else:
                stack.pop()
                depth -= 1
                if var:
                    ans += 2**depth
                var = False
        return ans

