import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        extra_hours = h - len(piles)
        k = piles[-1]

        min_k = math.ceil(piles[-1] / (extra_hours + 1))
        
        low = min_k
        high = piles[-1]
        while high >= low:
            middle = (high+low) // 2
            added_hours = 0
            for i in range(len(piles) - 1, -1, -1):
                added_hours_i = math.ceil(piles[i] / middle) - 1
                if added_hours_i <= 0:
                    break
                added_hours += added_hours_i
            
            if added_hours <= extra_hours:
                k = middle
                high = middle - 1
            else:
                low = middle + 1
        
        return k