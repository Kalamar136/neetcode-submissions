class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited_grid = [[False] * len(grid[0]) for a in range(len(grid))]
        island_num = 0

        def depth_first_search(i, j):
            if visited_grid[i][j] or grid[i][j] == "0":
                return
            visited_grid[i][j] = True
            if i>0:
                depth_first_search(i-1, j)
            if i<len(grid)-1:
                depth_first_search(i+1, j)
            if j>0:
                depth_first_search(i, j-1)
            if j<len(grid[0])-1:
                depth_first_search(i, j+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited_grid[i][j]:
                    island_num += 1
                    depth_first_search(i,j)
        
        return island_num