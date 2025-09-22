from collections import deque
        
class MovingAverage:

    def __init__(self, size: int):
        self.q = deque([])
        self.size = size
        self.total_sum = 0
        
    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.total_sum -= self.q.popleft()

        self.q.append(val)
        self.total_sum += val
        return self.total_sum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)