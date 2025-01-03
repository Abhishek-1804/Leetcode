class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        initial_price = prices[0]
        profit = 0

        for i in prices[1:]:
            if i < initial_price:
                initial_price = i
            
            profit = max(profit, i-initial_price)
        
        return profit
