class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        ans = []
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if digits[i] != 0 and i != j and i != k and j != k and digits[k] % 2 == 0:
                        ans.append(digits[i]*100+digits[j]*10+digits[k])

        return sorted(list(set(ans)))
