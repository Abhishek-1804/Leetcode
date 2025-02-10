class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_set = set()
        col_set = set()
        box_set = set()

        rows, cols = len(board), len(board[0])

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == '.':
                    continue

                if (board[row][col], row) in row_set or (board[row][col], col) in col_set or (board[row][col], (row//3, col//3)) in box_set:
                    return False
                
                row_set.add((board[row][col], row))
                col_set.add((board[row][col], col))
                box_set.add((board[row][col], (row//3, col//3)))
        
        return True