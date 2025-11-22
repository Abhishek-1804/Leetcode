class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        
        # Create a proper copy or use costs directly
        dp = [row[:] for row in costs]  # Deep copy
        
        for i in range(1, n):
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        
        return min(dp[n-1])
