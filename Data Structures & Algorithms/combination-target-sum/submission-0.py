class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination = []
        combination_sum = 0

        def backtracking_combinations(combination_l, combination_sum_l, current_multiple):
            if combination_sum_l > target:
                return
            elif combination_sum_l == target:
                combinations.append(combination_l.copy())
                return
            
            for i in range(current_multiple, len(nums)):
                combination_sum_l += nums[i]
                combination_l.append(nums[i])
                backtracking_combinations(combination_l, combination_sum_l, i)

                combination_sum_l -= nums[i]
                combination_l.pop()
            
        backtracking_combinations(combination, combination_sum, 0)

        return combinations