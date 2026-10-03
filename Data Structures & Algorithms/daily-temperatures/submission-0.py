class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Strategy: Populate the stack iteratively with temperature values pop them only when a higher temperature is reached
        result = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            # Peek at the top of the stack for temperatures of previous days
            while stack and t > stack[-1][1]:
                i_p, t_p = stack.pop()
                result[i_p] = i - i_p
            stack.append((i,t))
        
        return result