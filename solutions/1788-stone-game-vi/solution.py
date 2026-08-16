class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        arr = []
        a, b = 0, 0
        for i,j in zip(aliceValues,bobValues):
            a += i
            b += j
            arr.append([i,j])

        new_arr = sorted(arr, key=lambda x:x[0]+x[1], reverse=True)
        
        for idx, (i,j) in enumerate(new_arr):
            if idx % 2 == 0:
                b -= j
            else:
                a -= i

        if a > b:
            return 1
        if b > a:
            return -1
        return 0
