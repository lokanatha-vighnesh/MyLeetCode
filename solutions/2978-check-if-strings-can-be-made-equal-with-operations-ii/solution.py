class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        strings = [s1,s2]
        n = len(s1)
        for i in range(n):
            if s1[i] not in s2:
                return False
        
        even = {}
        odd = {}

        for i in range(n):
            if i % 2 == 0:
                if s2[i] in even:
                    even[s2[i]] += 1
                else:
                    even[s2[i]] = 1
            else:
                if s2[i] in odd:
                    odd[s2[i]] += 1
                else:
                    odd[s2[i]] = 1
        for i in range(n):
            if i % 2 == 0:
                if s1[i] in even:
                    even[s1[i]] -= 1
                else:
                    return False
            else:
                if s1[i] in odd:
                    odd[s1[i]] -= 1
                else:
                    return False
        for i in even.values():
            if i == 0:
                continue
            else:
                return False
        for i in odd.values():
            if i == 0:
                continue
            else:
                return False
        return True
