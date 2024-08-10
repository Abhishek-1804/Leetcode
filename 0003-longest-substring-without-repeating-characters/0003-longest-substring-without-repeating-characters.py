class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        maxLen = 0
        start, end = 0, 0

        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
            
            else:
                maxLen = max(maxLen, end-start)
                while s[start] != s[end]:
                    seen.remove(s[start])
                    start += 1

                seen.remove(s[start])
                start += 1
        
        maxLen = max(maxLen, end - start)
        
        return maxLen
