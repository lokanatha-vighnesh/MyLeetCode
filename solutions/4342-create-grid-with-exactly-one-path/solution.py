class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = ['#'*n for _ in range(m)]
        grid[0] = '.'*n
        for i in range(1,m):
            grid[i] = grid[i][:-1]+'.'
        return grid
