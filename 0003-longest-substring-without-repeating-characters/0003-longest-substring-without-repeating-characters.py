class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hMap = {}
        maxLen = 0
        left = 0

        for i in range(len(s)):
            if s[i] in hMap and hMap[s[i]] >= left:
                left = hMap[s[i]] + 1
            hMap[s[i]] = i
            maxLen = max(maxLen, i-left + 1)
        

        return maxLen