class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0
        string1 = ''
        string2 = ''
        count1,count2 = 0,0
        for i in range(n//2):
            string1 += '01'
            string2 += '10'
        if n % 2 == 1:
            if len(string1) > n:
                string1 = string1[:-1]
            else:
                string1 += '0' if string1[-1] == '1' else '1'
        if n % 2 == 1:
            if len(string2) > n:
                string2 = string2[:-1]
            else:
                string2 += '0' if string2[-1] == '1' else '1'

        for i in range(len(s)):
            if s[i] == string1[i]:
                count1 += 1
            if s[i] == string2[i]:
                count2 += 1
        return min(count1,count2)
