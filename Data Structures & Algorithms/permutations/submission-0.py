class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def backtracking_permutations(permutation, taken_array):
            if len(permutation) >= len(nums):
                permutations.append(permutation.copy())
                return
            
            for i in range(len(nums) - len(permutation)):
                index = self.indexNthOccurence(taken_array, False, i+1)
                taken_array[index] = True
                permutation.append(nums[index])

                backtracking_permutations(permutation, taken_array)

                taken_array[index] = False
                permutation.pop()
        
        backtracking_permutations([], [False] * len(nums))
        return permutations
    
    def indexNthOccurence(self, list1, item, n):
        start = 0
        for i in range(n):
            index = list1.index(item, start)
            start = index + 1
        return index