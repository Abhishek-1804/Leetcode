class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        h = {}
        left = 0
        ans = 0

        for i in range(len(s)):
            if s[i] in h and left <= h[s[i]]:
                left = h[s[i]] + 1
            h[s[i]] = i
            ans = max(ans, i-left+1)
            
        return ans