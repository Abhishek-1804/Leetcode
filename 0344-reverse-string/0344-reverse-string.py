class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        start, end = 0, len(s)-1

        while start < end:
            s[start] = ord(s[start]) ^ ord(s[end])
            s[end] = s[start] ^ ord(s[end])
            s[start] = s[start] ^ s[end]
            s[start] = chr(s[start])
            s[end] = chr(s[end])
            start += 1
            end -= 1