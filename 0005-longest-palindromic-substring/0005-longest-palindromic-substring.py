class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        resLen = 0

        for i in range(len(s)):
            #odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            if r-l+1 > resLen:
                res = s[l+1:r]
                resLen = r-l+1

            #even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                
            if r-l+1 > resLen:
                res = s[l+1:r]
                resLen = r-l+1
        
        return res
