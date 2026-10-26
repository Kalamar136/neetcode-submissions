class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # DP where we notice that the number of path to reach cell k
        # is just the sum of possible paths to reach cells above and left of k

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp_mem = [[0] * (m + 1) for row in range(n + 1)]
        dp_mem[0][1] = 1

        for i in range(n):
            for j in range(m):
                up = dp_mem[i][j + 1]
                left = dp_mem[i + 1][j]
                dp_mem[i + 1][j + 1] = up + left if obstacleGrid[i][j] == 0 else 0
        
        return dp_mem[n][m]