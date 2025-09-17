class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        for row in range(len(words)):
            for col in range(len(words[0])):
                if col >= len(words) or row >= len(words[col]) or words[row][col] != words[col][row]:
                    return False

        return True