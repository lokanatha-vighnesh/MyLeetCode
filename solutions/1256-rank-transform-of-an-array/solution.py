class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new_arr = list(set(arr))
        n = len(arr)
        new_arr.sort()
        hm = {j:i for i,j in enumerate(new_arr)}
        ans = [0]*n
        for i in range(n):
            ans[i] = hm[arr[i]]+1
        return ans

