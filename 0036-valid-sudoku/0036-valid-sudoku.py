class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows, cols = len(board), len(board[0])

        row_set = set()
        col_set = set()
        box_set = set()

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == '.':
                    continue
                    
                row_check = (board[row][col], row)
                col_check = (board[row][col], col)
                box_check = (board[row][col], row//3, col//3)

                if row_check in row_set or col_check in col_set or box_check in box_set:
                    return False
                row_set.add(row_check)
                col_set.add(col_check)
                box_set.add(box_check)
        
        return True