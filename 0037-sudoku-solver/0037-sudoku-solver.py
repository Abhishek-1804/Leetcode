class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(row, col, num):
            for i in range(0, 9):
                if board[row][i] == str(num):
                    return False
                if board[i][col] == str(num):
                    return False
            
            start_row = 3 * (row // 3)
            start_col = 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == str(num):
                        return False
            
            return True

        def backtrack(board):
            for row in range(len(board)):
                for col in range(len(board)):
                    if board[row][col] == '.':
                        for i in range(1, 10):
                            if is_valid(row, col, i):
                                board[row][col] = str(i)
                                if backtrack(board):
                                    return True
                                board[row][col] = '.'
                        return False
            return True
        
        if backtrack(board):
            return board