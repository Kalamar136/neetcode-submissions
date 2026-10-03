class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xorer = 0
        # First pass to impress all the numbers' information
        for num in nums:
            xorer ^= num
        
        # Second pass to discover the traitor by comparing with the xorer
        result = None
        for num in nums:
            if xorer ^ num == 0:
                result = num
                break
        
        return result