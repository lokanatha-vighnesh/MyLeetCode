class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        i = 0
        for i in range(k):
            top_row = x
            top_col = y+i
            down_row = x+k-1
            while top_row <= down_row:
                grid[top_row][top_col],grid[down_row][top_col] = grid[down_row][top_col],grid[top_row][top_col]
                top_row += 1
                down_row -= 1

        return grid
