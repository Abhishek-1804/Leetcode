class Solution:
    def rob(self, nums: List[int]) -> int:


        n = len(nums)
        
        dp = [None]*3

        dp[0] = nums[0]
        if n == 1:
            return nums[0]

        dp[1] = max(dp[0], nums[1])

        for i in range(2, n):
            dp[2] = max(dp[1], nums[i]+dp[0])
            dp.pop(0)
            dp.append(None)

        # p=[0]*(2)
        # p[1]=nums[0]
        # for i in range(1,n):
        # p[(i+1)&1]=max(p[(i-1)&1]+nums[i], p[i&1])
        # return p[n&1]

        return dp[1]