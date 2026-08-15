class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]] += 1
            else:
                d[arr[i]] = 1
        
        arr = []
        for i,j in d.items():
            if j == 1:
                arr.append(i)
        if k > len(arr):
            return ''
        return arr[k-1]
