class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Recursive Backtracking trying every unique number at each spot consecutively

        perm_size = len(nums)
        nums_stats = {}
        for num in nums:
            nums_stats[num] = nums_stats.get(num, 0) + 1

        nums_unique = list(nums_stats.keys())

        answer = []
        def perm_bt(l, l_stats):
            if len(l) >= perm_size:
                answer.append(l.copy())
                return
            
            for num in nums_unique:
                if nums_stats[num] - l_stats.get(num, 0) > 0:
                    l_stats[num] = l_stats.get(num, 0) + 1
                    perm_bt(l + [num], l_stats)
                    l_stats[num] -= 1
        
        perm_bt([], {})
        
        return answer