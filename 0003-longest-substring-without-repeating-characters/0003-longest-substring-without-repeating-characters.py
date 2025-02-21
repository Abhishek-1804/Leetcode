class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        h = {}
        start = 0
        maxLen = 0

        for i in range(len(s)):

            if s[i] in h and h[s[i]] >= start:
                start = h[s[i]] + 1
            
            h[s[i]] = i
            maxLen = max(maxLen, i-start+1)
        
        return maxLen
