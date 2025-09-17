class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        for row in range(len(words)):
            for col in range(len(words[row])):
                if words[row][col] != words[col][row]:
                    return False

        return True