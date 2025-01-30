class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        starts = [float('inf')] * 26
        ends = [float('-inf')] * 26

        ans = 0

        for i in range(len(s)):
            char_pos = ord(s[i]) - ord('a')
            starts[char_pos] = min(starts[char_pos], i)
            ends[char_pos] = max(ends[char_pos], i)
        
        for i, j in zip(starts, ends):
            if i != float('inf') and j != float('-inf'):
                middle_chars = set(s[i+1:j])
                ans += len(middle_chars)
        
        return ans