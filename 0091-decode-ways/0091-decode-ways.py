class Solution:
    def numDecodings(self, s: str) -> int:
        # return self.numDecodings_1(s)
        return self.numDecodings_2(s)

    def numDecodings_2(self, s: str) -> int:
    
        dp = [0 for i in range(len(s) + 1)]

        dp[0] = 1

        if s[0] == '0':
            return 0

        else:
            dp[1] = 1

        for i in range(2, len(s)+1):
            if s[i-1] == '0':
                if s[i-2] == '1' or s[i-2] == '2':
                    dp[i] = dp[i-2]

                else:
                    return 0

            else:
                if (s[i-2] == '1') or (s[i-2] == '2' and int(s[i-1]) < 7):
                    dp[i] = dp[i-1] + dp[i-2]

                else:
                    dp[i] = dp[i-1]

        return dp[len(s)]

    def numDecodings_1(self, s: str) -> int:
        
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
                
            if s[i] == '0':
                return 0
            
            res = dfs(i+1)
            if (i+1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456'))):
                res += dfs(i+2)
            
            dp[i] = res
            return res

        return dfs(0)