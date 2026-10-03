class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []
        nums.sort()
        self.nums = nums

        self.subset_backtracking([], 0)

        return self.subsets

    
    def subset_backtracking(self, subset, i):
        if i >= len(self.nums):
            self.subsets.append(subset.copy())
            return
        
        # First consider subsets with element i
        subset.append(self.nums[i])
        i += 1
        self.subset_backtracking(subset, i)

        # Then consider subsets without element i
        subset.pop()
        if i-2 < 0 or not (self.nums[i-1] == self.nums[i-2] and subset and subset[-1] == self.nums[i-1]):
            self.subset_backtracking(subset, i)
        i -= 1
