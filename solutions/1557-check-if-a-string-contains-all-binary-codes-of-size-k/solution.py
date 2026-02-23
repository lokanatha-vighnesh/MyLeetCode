class Solution(object):
    def hasAllCodes(self, s, k):
        n = len(s)
        required_len = 2**k
        combinations = set()
        for i in range(n-k+1):
            string = s[i:i+k]
            combinations.add(string)

        return len(combinations)==required_len
