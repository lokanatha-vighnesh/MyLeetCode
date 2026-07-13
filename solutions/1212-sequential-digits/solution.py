class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        min_len = len(str(low))
        max_len = len(str(high))
        num = '123456789'
        ans = []
        for i in range(min_len,max_len+1):
            for j in range(9):
                n = int(num[j:j+i])
                if n >= low and n <= high and n not in ans:
                    ans.append(n)
                else:
                    continue


        return ans
