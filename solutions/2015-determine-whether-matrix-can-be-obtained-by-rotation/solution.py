from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        if mat == target:
            return True

        rot90 = [[0]*n for _ in range(n)]
        rot180 = [[0]*n for _ in range(n)]
        rot270 = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rot90[i][j] = mat[n - 1 - j][i]
                rot180[i][j] = mat[n - 1 - i][n - 1 - j]
                rot270[i][j] = mat[j][n - 1 - i]

        if (target == rot90) or (target == rot180) or (target == rot270):
            return True

        return False
