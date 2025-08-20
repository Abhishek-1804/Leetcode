class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        s_len = len(s)
        char_ind = {}
        i = 0
        answer = float('-inf')

        for j in range(s_len):
            char_ind[s[j]] = j

            if len(char_ind) > 2:
                drop_char = min(char_ind, key=char_ind.get)
                i = char_ind[drop_char] + 1
                del char_ind[drop_char]

            answer = max(answer, j - i + 1)

        return answer