class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[None for _ in range(n)] for _ in range(n)]
        

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        if (
            self.win_row(row, player) or
            self.win_col(col, player) or
            self.win_diag(player) or
            self.win_antidiag(player)
        ):
            return player
        return 0

    def win_row(self, row, player):
        for c in range(self.n):
            if self.board[row][c] != player:
                return False
        return True

    def win_col(self, col, player):
        for r in range(self.n):
            if self.board[r][col] != player:
                return False
        return True

    def win_diag(self, player):
        for i in range(self.n):
            if self.board[i][i] != player:
                return False
        return True

    def win_antidiag(self, player):
        for i in range(self.n):
            if self.board[i][self.n - 1 - i] != player:
                return False
        return True

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)