import heapq

class Leaderboard:
    def __init__(self):
        self.leaderboard = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.leaderboard:
            self.leaderboard[playerId] = 0
        self.leaderboard[playerId] += score

    def top(self, K: int) -> int:
        # heapq.nlargest returns the K largest elements from the iterable
        return sum(heapq.nlargest(K, self.leaderboard.values()))
    
    def reset(self, playerId: int) -> None:
        self.leaderboard[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)