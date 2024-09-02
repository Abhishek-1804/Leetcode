class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()
        
        def backtrack(i, j, pos):
            if pos == len(word):
                return True
            
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i, j) in visited or board[i][j] != word[pos]:
                return False
            
            visited.add((i, j))
            
            # Explore all four possible directions
            if (backtrack(i-1, j, pos + 1) or  # Up
                backtrack(i+1, j, pos + 1) or  # Down
                backtrack(i, j-1, pos + 1) or  # Left
                backtrack(i, j+1, pos + 1)):   # Right
                return True
            
            visited.remove((i, j))
            return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0): return True
        
        return False