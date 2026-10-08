class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        n = len(s)
        left, right = 0, 0
        val = 0
        ans = []
        i = 0
        while True:
            if s[i] == '(':
                val += 1
            else:
                val -= 1
            right += 1
            if val == 0:
                ans.append([left,right])
                left = right
            i += 1
            if i >= n:
                break
        print(ans)
        string = ''
        for i,j in ans:
            string = string + s[i+1:j-1]
        return string
