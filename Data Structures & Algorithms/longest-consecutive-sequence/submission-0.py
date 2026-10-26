class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Building map of consecutive numbers
        map_num = {}
        for num in nums:
            if num not in map_num:
                map_num[num] = (num-1 in map_num, num+1 in map_num)
                if num - 1 in map_num:
                    map_num[num - 1] = (map_num[num - 1][0], True)
                if num + 1 in map_num:
                    map_num[num + 1] = (True, map_num[num + 1][1])
        
        # Traverse the dictionary
        traversed = set()
        max_seq = 1
        for num in map_num:
            if not map_num[num][0] and map_num[num][1]:
                current_num = num
                seq_len = 1
                while map_num[current_num][1]:
                    current_num = current_num + 1
                    seq_len += 1
                
                if seq_len > max_seq:
                    max_seq = seq_len
        
        return max_seq