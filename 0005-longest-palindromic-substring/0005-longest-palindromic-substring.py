class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_len = 0
        output = ''
        n = len(s)

        for i in range(n):

            start, end = i, i
            while start >= 0 and end < n and s[start] == s[end]:
                if end - start + 1 > max_len:
                    max_len = end - start + 1
                    output = s[start:end+1]
                start -= 1
                end += 1
            
            start, end = i, i+1
            while start >= 0 and end < n and s[start] == s[end]:
                if end - start + 1 > max_len:
                    max_len = end - start + 1
                    output = s[start:end+1]
                start -= 1
                end += 1
            
        
        return output