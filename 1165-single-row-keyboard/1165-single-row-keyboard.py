class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        answer = 0
        prev_ind = 0

        for char in word:
            char_ind = keyboard.index(char)
            answer += abs(prev_ind - char_ind)
            prev_ind = char_ind


        return answer
