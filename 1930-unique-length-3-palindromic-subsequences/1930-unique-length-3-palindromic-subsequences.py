class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        min_exist = [float('inf')] * 26
        max_exist = [float('-inf')] * 26

        for i in range(len(s)):
            char_index = ord(s[i]) - ord('a')
            min_exist[char_index] = min(min_exist[char_index], i)
            max_exist[char_index] = max(max_exist[char_index], i)
        
        ans = set()

        for char_index in range(26):
            if min_exist[char_index] != float('inf') and max_exist[char_index] != float('-inf'):
                for j in range(min_exist[char_index] + 1, max_exist[char_index]):
                    if s[min_exist[char_index]] + s[j] + s[max_exist[char_index]] not in ans:
                        ans.add(s[min_exist[char_index]] + s[j] + s[max_exist[char_index]])
        
        return len(ans)