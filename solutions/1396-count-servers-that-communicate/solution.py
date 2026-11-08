class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        total, isolated = 0, 0
        row = [sum(i) for i in grid]
        col = [0]*n
        for co in range(n):
            c = 0
            for ro in range(m):
                if grid[ro][co] == 1:
                    c += 1
            col[co] = c
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total += 1
                    if row[i] == 1 and col[j] == 1:
                        isolated += 1
                else:
                    continue
        return total - isolated


