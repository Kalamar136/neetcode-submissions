class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Strategy: Take the product of all numbers then divide by nums[i] for each output[i]
        # It is O(n) time complexity wise and in space complexity

        # 3 cases:
        # 1- No 0's in the list -> Compute overall product then divide for each index
        # 2- One 0 in the list -> Compute the overall product without the only 0 in the list
        # 3- More than one 0 in the list -> 0 output for all
        zeros_indices = []
        product = 1
        for j in range(len(nums)):
            num = nums[j]
            if num != 0:
                product *= num
            else:
                zeros_indices += [j]
        
        # Case 1: no 0's
        if not zeros_indices:
            output = []
            for i in nums:
                output.append(product // i)
        # Case 3, all 0's:
        elif len(zeros_indices) > 1:
            output =  [0] * len(nums)
        # Case 2, one 0:
        else:
            output = [0] * len(nums)
            output[zeros_indices[0]] = product
        
        return output