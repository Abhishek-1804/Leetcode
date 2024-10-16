class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        import re

        # splitting alphabets and numbers
        split_ = re.findall(r'[a-zA-Z]|\d+', abbr)
        split_ind, word_ind = 0, 0

        while split_ind < len(split_) and word_ind < len(word):
            if split_[split_ind].isalpha():
                if word[word_ind] != split_[split_ind]:
                    return False
                else:
                    word_ind += 1
                    split_ind += 1
            
            else:
                if int(split_[split_ind]) == 0:
                    return False
                    
                if split_[split_ind] != str(int(split_[split_ind])):
                    return False
                # Skip characters in word based on the number
                word_ind += int(split_[split_ind])
                split_ind += 1

                # Boundary check
                if word_ind > len(word):
                    return False

        # Both indices should reach the end
        return split_ind == len(split_) and word_ind == len(word)

