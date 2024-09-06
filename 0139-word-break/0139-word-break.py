class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False]*len(s)

        start = 0

        for i in range(1, len(dp)+1):
            if s[start:i] in wordDict:
                dp[i-1] = True
                start = i
        
        return dp[-1]