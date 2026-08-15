class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        size = 10
        n = len(s)
        d = set()
        ans = set()
        for i in range(n-size+1):
            string = s[i:i+size]
            if string in d:
                ans.add(string)
            else:
                d.add(string)

        return list(ans)
