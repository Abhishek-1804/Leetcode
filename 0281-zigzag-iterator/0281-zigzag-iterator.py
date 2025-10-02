from typing import List

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.turn = 0  # 0 for v1, 1 for v2

    def next(self) -> int:
        if not self.hasNext():
            return
        if self.turn == 0 and self.v1:
            self.turn = 1
            return self.v1.pop(0)
        elif self.v2:
            self.turn = 0
            return self.v2.pop(0)
        elif self.v1:
            # only v1 left
            self.turn = 1
            return self.v1.pop(0)

    def hasNext(self) -> bool:
        return len(self.v1) > 0 or len(self.v2) > 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())