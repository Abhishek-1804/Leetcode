class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(board, row, col, num):
            # Check if the number exists in the row
            for i in range(9):
                if board[row][i] == num:
                    return False
            
            # Check if the number exists in the column
            for i in range(9):
                if board[i][col] == num:
                    return False
            
            # Check if the number exists in the 3x3 subgrid
            start_row = 3 * (row // 3)
            start_col = 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == num:
                        return False
            
            return True

        def backtrack(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(board, row, col, num):
                                board[row][col] = num
                                if backtrack(board):  # If the board is solvable from here, return True
                                    return True
                                board[row][col] = '.'  # Otherwise, undo the placement (backtrack)
                        return False  # No valid number found, so return False
            return True  # Solved
        
        backtrack(board)
        return board
        