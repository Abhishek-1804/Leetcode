class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
    
        rows, cols = len(board), len(board[0])
        visited = set()
    
        def dfs(row, col):
            temp = set()
            stack = [(row, col)]
            surrounded = True
            while stack:
                r, c = stack.pop()
                if (r, c) not in temp:
                    temp.add((r, c))
                    if r == 0 or c == 0 or r == rows - 1 or c == cols - 1:
                        surrounded = False
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in temp and board[nr][nc] == "O":
                            stack.append((nr, nc))
    
            if surrounded:
                for r, c in temp:
                    board[r][c] = 'X'
            else:
                visited.update(temp)
    
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and (row, col) not in visited:
                    dfs(row, col)
    
        return
    