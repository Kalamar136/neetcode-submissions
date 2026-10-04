class Solution:
    def rob(self, nums: List[int]) -> int:
        # The max amount of money that can be robbed up to house i is max(max_rob(i-1), max_rob(i-2) + nums[i])

        # Initialize max_rob for robbing no houses (max_rob[0] = 0) and robbing up to the first house (max_rob[1] = nums[0])
        max_rob_prev = 0
        max_rob = nums[0]

        # Iterate through the houses and compute max_rob up to house i iteratively
        for i in range(1, len(nums)):
            max_rob_tmp = max_rob
            max_rob = max(max_rob, max_rob_prev + nums[i])
            max_rob_prev = max_rob_tmp
        
        return max_rob

