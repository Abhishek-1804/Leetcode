class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        word_length = len(word)

        def backtrack(row, col, ind):

            if ind == word_length:
                return True
            
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[ind]:
                return False

            temp = board[row][col]
            board[row][col] = '#'
            if (backtrack( row+1, col, ind+1 ) or 
                backtrack( row-1, col, ind+1 ) or
                backtrack( row, col+1, ind+1 ) or
                backtrack( row, col-1, ind+1 )):
                return True

            board[row][col] = temp
            
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):
                        return True
        
        return False