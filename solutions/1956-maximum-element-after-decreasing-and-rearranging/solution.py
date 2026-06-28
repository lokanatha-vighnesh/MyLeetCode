class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr = sorted(arr)
        for i in range(1,n):
            if abs(arr[i]-arr[i-1]) <= 1:
                continue
            else:
                arr[i] = arr[i-1]+1
        a = max(arr)
        return a if a < n else n
