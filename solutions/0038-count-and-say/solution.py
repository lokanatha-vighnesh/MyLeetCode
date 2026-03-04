class Solution(object):
    def pairer(self, s):
        if not s: return []
        pairs = []
        element = s[0]
        count = 1
        
        for i in range(1, len(s)):
            if s[i] == element:
                count += 1
            else:
                pairs.append([element, count])
                element = s[i]
                count = 1
        
        # Crucial: append the final group after the loop
        pairs.append([element, count])
        return pairs

    def stringMaker(self, pairs):
        res = ""
        for p in pairs:
            # Format: [count][value] -> Append to the RIGHT
            res += f"{p[1]}{p[0]}"
        return res

    def countAndSay(self, n):
        if n == 1:
            return "1"
        # Recursive step: get previous string -> pair it -> build new string
        return self.stringMaker(self.pairer(self.countAndSay(n - 1)))
