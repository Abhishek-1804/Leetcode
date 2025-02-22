class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        output = 0
        stock = prices[0]

        for num in prices[1:]:
            if num < stock:
                stock = num
            output = max(output, num-stock)

        return output