class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        one_d_board = [0]
        n = len(board)
        
        for row in range(len(board)-1, -1, -1):
            if (n - 1 - row) % 2 == 0:
                for col in range(len(board)):
                    one_d_board.append(board[row][col])
            else:
                for col in range(len(board)-1, -1, -1):
                    one_d_board.append(board[row][col])
        
        q = collections.deque([(1,0)])
        visit = set([1])
        while q:
            index, moves = q.popleft()
            
            for inc in range(1,7):
                nextSquare = index + inc
                if nextSquare > n * n:
                    break
            
                square_val = one_d_board[nextSquare]
                if square_val != -1:
                    nextSquare = square_val
        
                if nextSquare == n * n:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append((nextSquare, moves + 1))
        
        return -1