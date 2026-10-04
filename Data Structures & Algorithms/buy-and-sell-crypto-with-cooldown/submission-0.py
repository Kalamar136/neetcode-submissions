class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # At each day, if no NeetCoin -> I can buy today's NeetCoin and wait for a day or idle
        # If NeetCoin -> I can sell or idle
        # At day i the max profit if NeetCoin at end of day max(profit_max(i-2)(c=0) - prices(i), profit_max(i-1)(c=1)) 
        # If no NeetCoin at end of day: max(profit_max(i-1)(c=1) + prices(i), profit_max(i-1)(c=0))

        # Edge case: 1 day of trading
        if len(prices) == 1:
            return 0

        # Initialize 2D max_profit array:
        max_profit = [[0] * len(prices) for _ in range(2)]
        max_profit[1][0] = -prices[0]
        max_profit[1][1] = max(-prices[0], -prices[1])

        # Iterate over days
        for j in range(1, len(max_profit[0])):
            # If I have a NeetCoin, then I bought it yesterday or I still have it from yesterday (except for day 2)
            # NeetCoin at the end of day case
            if j >= 2:
                max_profit[1][j] = max(max_profit[0][j-2] - prices[j], max_profit[1][j-1])
            # No NeetCoin at the end of day
            max_profit[0][j] = max(max_profit[1][j-1] + prices[j], max_profit[0][j-1])
        
        return max_profit[0][len(max_profit[0])-1]