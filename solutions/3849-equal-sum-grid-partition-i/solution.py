class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row_sum = [sum(i) for i in grid]
        col_sum = []
        for i in range(len(grid[0])):
            col = 0
            for j in range(len(grid)):
                col += grid[j][i]
            col_sum.append(col)
        row = row_sum[0]
        total = sum(row_sum)
        for i in range(1,len(row_sum)):
            if row == total - row:
                return True
            else:
                row += row_sum[i]
        c = col_sum[0]
        for i in range(1,len(col_sum)):
            if c == total - c:
                return True
            else:
                c += col_sum[i]
        return False
