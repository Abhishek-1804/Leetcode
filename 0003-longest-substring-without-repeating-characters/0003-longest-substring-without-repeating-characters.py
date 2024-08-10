class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIndexMap = {}
        left = max_len = 0

        for right, char in enumerate(s):
            if char in charIndexMap and charIndexMap[char] >= left:
                left = charIndexMap[char] + 1
            charIndexMap[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len