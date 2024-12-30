class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        h = collections.defaultdict(int)
        max_count = 0  # To store the max frequency of a character in the window
        max_len = 0
        left = 0

        for right in range(len(s)):
            h[s[right]] += 1
            max_count = max(max_count, h[s[right]])

            if (right-left+1)-max_count > k:
                h[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len