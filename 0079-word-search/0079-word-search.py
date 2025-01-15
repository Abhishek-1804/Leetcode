class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(row, col, pos):
            if pos == len(word):
                return True
            
            if (0 <= row < rows and 
                0 <= col < cols and 
                (row, col) not in visited and 
                board[row][col] == word[pos]):

            
                visited.add((row, col))

                if (dfs(row-1, col, pos + 1) or  # Up
                    dfs(row+1, col, pos + 1) or  # Down
                    dfs(row, col-1, pos + 1) or  # Left
                    dfs(row, col+1, pos + 1)):   # Right
                    return True
            
                visited.remove((row, col))

            return False
            
        for row in range(rows):
            for col in range(cols):
                if word[0] == board[row][col]:
                    if dfs(row, col, 0):
                        return True
                    
        return False