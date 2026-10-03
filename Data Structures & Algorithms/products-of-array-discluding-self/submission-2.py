class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Strategy: Precompute prefix and suffix products and use them to compute the final output
        # It is O(n) time complexity wise and in space complexity

        # Iterate through the nums list and populate prefix and suffix lists
        # We add dummy bounds to the prefix and suffix lists for simplifying the code
        prefix = [1] + nums.copy()
        suffix = nums.copy() + [1]
        for i in range(1, len(nums)):
            prefix[i] *= prefix[i-1]
            suffix[-1-i] *= suffix[-i]
        
        # Iterate through the prefix and suffix lists to create output
        output = nums.copy()
        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i+1]
        
        return output