class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        board.reverse()

        def intToPos(square):
            r, c = (square - 1) // n, (square - 1) % n
            if r % 2:
                c = n - 1 - c
            return (r, c)

        q = collections.deque([(1,0)])
        visit = set()
        while q:
            square, moves = q.popleft()
            
            for inc in range(1,7):
                nextSquare = square + inc

                r,c = intToPos(nextSquare)
                square_val = board[r][c]

                if square_val != -1:
                    nextSquare = square_val
        
                if nextSquare == n * n:
                    return moves + 1

                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append((nextSquare, moves + 1))
        
        return -1