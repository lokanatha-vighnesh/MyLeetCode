class Solution:
    def maxProduct(self, n: int) -> int:
        arr = []
        while n > 0:
            v = n % 10
            arr.append(v)
            n = n // 10
        first_max = 0
        second_max = 0
        for i in range(len(arr)):
            if arr[i] > first_max:
                second_max = first_max
                first_max = arr[i]
            elif arr[i] > second_max and arr[i] <= first_max:
                second_max = arr[i]
        return first_max*second_max
