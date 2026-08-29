class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        ans = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ans[i][j] = matrix[j][n-i-1]

        for i in range(n):
            ans[i] = ans[i][::-1]
        matrix[:] = ans[::-1][:]
