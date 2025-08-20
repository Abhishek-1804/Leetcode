class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        s_len = len(s)
        char_ind = {}
        i = 0
        answer = float('-inf')

        for j in range(s_len):
            char_ind[s[j]] = j

            if len(char_ind) > 2:
                del_index = min(char_ind.values())
                del_char = [c for c, idx in char_ind.items() if idx == del_index][0]
                del char_ind[del_char]
                i = del_index + 1

        
            answer = max(answer, j - i + 1)
            
        return answer
