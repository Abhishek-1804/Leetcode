class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        max_len = 0

        h = {}

        for i in range(len(s)):
            
            if s[i] in h and left <= h[s[i]]:
                left = h[s[i]]+1
            
            h[s[i]] = i
            max_len = max(max_len, i-left+1)

        return max_len