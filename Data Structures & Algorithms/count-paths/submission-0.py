class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid_metadata = [[0 for _ in range(n)] for _ in range(m)]
        grid_metadata[0][0] = 1
        
        for row in range(m):
            for col in range(n):
                if row - 1 >= 0:
                    grid_metadata[row][col] += grid_metadata[row-1][col]
                if col - 1 >= 0:
                    grid_metadata[row][col] += grid_metadata[row][col-1]
        return grid_metadata[m-1][n-1]