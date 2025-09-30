class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        import heapq

        cost = 0
        n = len(sticks)

        if n < 2:
            return cost

        heapq.heapify(sticks)

        while n >= 2:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            cost += x + y
            heapq.heappush(sticks, x+y)
            n -= 1
        
        return cost