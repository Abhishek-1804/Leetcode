from collections import deque

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.q = deque()
        self.count = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.q and self.count[self.q[0]] > 1:
            self.q.popleft()
        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        if value not in self.count:
            self.q.append(value)
        self.count[value] = self.count.get(value, 0) + 1
