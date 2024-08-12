class Solution:
    def helper(self, board, row, col) -> int:
        # returns number of 1's around the cell

        dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        count = 0
        for r, c in dir:
            new_row = row+r
            new_col = col+c
            if new_row >= 0 and new_col >= 0 and new_row < len(board) and new_col < len(board[0]):
                count += board[new_row][new_col][0]
        
        return count

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # add booleans to values
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 1:
                    board[row][col] = [board[row][col], True]
                elif board[row][col] == 0:
                    board[row][col] = [board[row][col], False]
        
        # change booleans
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col][0] == 0:
                    if self.helper(board, row, col) == 3:
                        board[row][col][1] = True
                
                else:
                    if self.helper(board, row, col) < 2 or self.helper(board, row, col) > 3:
                        board[row][col][1] = False
        
        # change values according to booleans
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col][1] == True:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
        