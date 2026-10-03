class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lower = 0
        higher = len(numbers) - 1
        while numbers[lower] + numbers[higher] != target:
            if numbers[lower] + numbers[higher] < target:
                lower += 1
            else:
                higher -= 1
        return [lower+1, higher+1]