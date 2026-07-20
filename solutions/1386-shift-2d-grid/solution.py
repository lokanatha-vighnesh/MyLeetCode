class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(grid[0])
        m = len(grid)
        
        arr = []
        for i in range(m):
            arr += grid[i]

        arr = arr[-(k%(m*n)):] + arr[:-(k%(m*n))]
        ans = []
        j = 0
        for i in range(m):
            ans.append(arr[j:j+n])
            j += n
        return ans
        
