class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Initialize arrays to track first and last occurrences of each character
        first_occurrence = [-1] * 26
        last_occurrence = [-1] * 26
        
        # Populate first and last occurrence arrays
        for i, char in enumerate(s):
            char_index = ord(char) - ord('a')
            if first_occurrence[char_index] == -1:
                first_occurrence[char_index] = i
            last_occurrence[char_index] = i
        
        # Set to count unique palindromic subsequences
        unique_count = 0
        
        # Iterate through each character ('a' to 'z')
        for char_index in range(26):
            start = first_occurrence[char_index]
            end = last_occurrence[char_index]
            
            # If valid start and end are found
            if start != -1 and end > start:
                # Collect all unique middle characters
                middle_chars = set(s[start + 1:end])
                unique_count += len(middle_chars)
        
        return unique_count
