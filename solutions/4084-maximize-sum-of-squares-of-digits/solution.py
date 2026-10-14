class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        string = [0]*num
        dup = sum
        ans = 0
        i = 0
        while sum > 0 and i < num:
            if sum >= 9:
                string[i] = 9
                ans += 9
                sum -= 9
            else:
                string[i] = sum
                ans += sum
                sum -= sum
            i += 1
        if ans != dup:
            return ''
        return ''.join(map(str, string))

