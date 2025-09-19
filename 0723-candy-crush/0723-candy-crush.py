class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        rows = len(board)
        cols = len(board[0])

        def find():
            crushed_set = set()

            # check vertically
            for row in range(1, rows-1):
                for col in range(cols):
                    if board[row][col] == 0:
                        continue
                    if board[row][col] == board[row-1][col] == board[row+1][col]:
                        crushed_set.add((row, col))
                        crushed_set.add((row-1, col))
                        crushed_set.add((row+1, col))
            
            # check horizontally
            for row in range(rows):
                for col in range(1, cols-1):
                    if board[row][col] == 0:
                        continue
                    if board[row][col] == board[row][col-1] == board[row][col+1]:
                        crushed_set.add((row, col))
                        crushed_set.add((row, col+1))
                        crushed_set.add((row, col-1))
            
            return crushed_set

        def crush(crushed_set):
            for row, col in crushed_set:
                board[row][col] = 0
        
        def drop():
            for col in range(cols):
                lowest_zero = -1

                for row in range(rows-1, -1, -1):
                    if board[row][col] == 0:
                        lowest_zero = max(lowest_zero, row)
                    elif lowest_zero >= 0:
                        board[row][col], board[lowest_zero][col] = board[lowest_zero][col], board[row][col]
                        lowest_zero -= 1
        
        crushed_set = find()
        while crushed_set:
            crush(crushed_set)
            drop()
            crushed_set = find()

        return board
            
            

