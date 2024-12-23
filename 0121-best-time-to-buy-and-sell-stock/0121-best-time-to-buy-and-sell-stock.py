class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        curr_buy, curr_profit, max_profit = prices[0], 0, 0

        for num in prices[1:]:
            if num < curr_buy:
                curr_buy = num
            curr_profit = num-curr_buy
            max_profit = max(max_profit, curr_profit)

        return max_profit