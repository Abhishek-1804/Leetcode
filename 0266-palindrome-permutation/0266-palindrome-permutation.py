class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        d = {}

        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
                if d[char] == 2:
                    del d[char]
        
        return len(d) <= 1
