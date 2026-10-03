class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0] * (len(text1) + 1) for a in range(len(text2)+1)]

        for i in range(len(text2)):
            for j in range(len(text1)):
                if text2[i] == text1[j]:
                    grid[i+1][j+1] = grid[i][j] + 1
                else:
                    grid[i+1][j+1] = max(grid[i+1][j], grid[i][j+1])
        print(grid)
        return grid[len(text2)][len(text1)]