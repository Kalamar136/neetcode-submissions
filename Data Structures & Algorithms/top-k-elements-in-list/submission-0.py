class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        int_dict = {}
        for i in nums:
            int_dict[i] = int_dict.get(i, 0) + 1
        sorted_dict = sorted(list(int_dict.items()), key=lambda tup: tup[1], reverse = True)
        return list(map(lambda tup: tup[0], sorted_dict[:k]))