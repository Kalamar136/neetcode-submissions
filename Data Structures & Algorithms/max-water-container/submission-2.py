class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # The volume of water is computed: smallest_bar_chosen * distance_between_bars_chosen
        # Strategy: Start by pointing at the 2 furthest bars
        # At each step, compute the water container
        # Then choose which pointer to move depending on which one will result in a larger water container (randomly break ties)

        bar1 = 0
        bar2 = len(heights)-1
        max_water = -1

        while bar2 != bar1:
            volume = (bar2 - bar1) * min(heights[bar1], heights[bar2])
            if volume > max_water:
                max_water = volume

            if heights[bar1] > heights[bar2]:
                bar2 -= 1
            elif heights[bar2] > heights[bar1]:
                bar1 += 1
            elif heights[bar1+1] > heights[bar2-1]:
                bar2 -= 1
            else:
                bar1 += 1
        
        return max_water