class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = len(board)
        col = len(board[0])

        row_set = set()
        col_set = set()
        box_set = set()
        
        for i in range(row):
            for j in range(col):
                val = board[i][j]
                if val == '.':
                    continue
                if (i, val) in row_set or (j, val) in col_set or ((i//3, j//3), val) in box_set:
                    return False
                row_set.add((i, val))
                col_set.add((j, val))
                box_set.add(((i//3, j//3), val))

        return True