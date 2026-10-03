class Solution:
    def climbStairs(self, n: int) -> int:
        staircase_array = [0] * (n+1)
        staircase_array[0] = 1
        staircase_array[1] = 1

        for i in range(2,n+1):
            staircase_array[i] = staircase_array[i-1] + staircase_array[i-2]
        
        return staircase_array[n]
