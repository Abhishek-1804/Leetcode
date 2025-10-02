import heapq
class Leaderboard:

    def __init__(self):
        self.leaderboard = {}
        
    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leaderboard:
            self.leaderboard[playerId] = 0
        self.leaderboard[playerId] += score

    def top(self, K: int) -> int:
        total = 0

        items = list(self.leaderboard.items())
        temp_list = [(v, k) for k, v in items]
        temp_list.sort(reverse = True)

        for i in range(K):
            total += temp_list[i][0]
        
        return total

    def reset(self, playerId: int) -> None:
        self.leaderboard[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)