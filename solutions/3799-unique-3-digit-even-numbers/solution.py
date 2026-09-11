class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        ans = []
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if digits[i] != 0 and i != j and i != k and j != k and digits[k] % 2 == 0:
                        ans.append(str(digits[i])+str(digits[j])+str(digits[k]))

        return len(set(ans))
