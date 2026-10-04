class Solution:
    def rob(self, nums: List[int]) -> int:
        # The max amount of money that can be robbed up to house i is max(max_rob(i-1), max_rob(i-2) + nums[i])

        # Initialize max_rob for robbing no houses (max_rob[0] = 0) and robbing up to the first house (max_rob[1] = nums[0])
        max_rob = [0] + nums.copy()

        # Iterate through the houses and compute max_rob up to house i iteratively
        for i in range(1, len(nums)):
            max_rob[i + 1] = max(max_rob[i], max_rob[i-1] + nums[i])
        
        return max_rob[len(nums)]

