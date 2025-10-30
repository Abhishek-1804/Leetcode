class Solution:
    def firstUniqChar(self, s: str) -> int:

        from collections import Counter

        counts = Counter(s)

        for i in range(len(s)):
            if counts[s[i]] == 1:
                return i
        
        return -1