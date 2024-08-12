class Solution:
    def helper(self, board, row, col) -> int:
        # returns number of 1's around the cell

        dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        count = 0
        for r, c in dir:
            new_row = row+r
            new_col = col+c
            if new_row >= 0 and new_col >= 0 and new_row < len(board) and new_col < len(board[0]) and abs(board[new_row][new_col]) == 1:
                count += 1
        
        return count

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                live_neighbors = self.helper(board, row, col)
                
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1

                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 2:
                    board[row][col] = 1
                elif board[row][col] == -1:
                    board[row][col] = 0
        