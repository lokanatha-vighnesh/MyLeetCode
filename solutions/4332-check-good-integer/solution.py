class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        s = str(n)
        digitSum = 0
        squareSum = 0
        for i in s:
            digitSum += int(i)
            squareSum += int(i)**2

        if squareSum-digitSum >= 50:
            return True
        return False
