class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr = [[abs(i-j) for j in arr2] for i in arr1]
        count = 0
        for i in arr:
            for j in i:
                if j > d:
                    continue
                else:
                    count -= 1
                    break
                
            count += 1
        return count
