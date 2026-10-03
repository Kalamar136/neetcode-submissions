class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            subsets_copy = subsets.copy()
            for subset in subsets_copy:
                subset_copy = subset.copy()
                subsets.append(subset_copy)
                subset_copy.append(num)
        
        return subsets