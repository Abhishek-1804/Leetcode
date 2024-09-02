class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, counter):
            if counter == len(word):
                return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[counter]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            
            found = (dfs(r + 1, c, counter + 1) or
                     dfs(r - 1, c, counter + 1) or
                     dfs(r, c + 1, counter + 1) or
                     dfs(r, c - 1, counter + 1))
            
            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False