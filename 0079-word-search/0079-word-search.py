class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(row, col, i):
            if i == len(word):
                return True
            
            if 0 <= row < rows and 0 <= col < cols and (row, col) not in visited and board[row][col] == word[i]:
                visited.add((row, col))

                if (
                    dfs(row+1, col, i+1) or 
                    dfs(row-1, col, i+1) or 
                    dfs(row, col+1, i+1) or 
                    dfs(row, col-1, i+1)
                ):
                    return True

                visited.remove((row, col))
            
            return False
        
        rows, cols = len(board), len(board[0])
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        
        return False