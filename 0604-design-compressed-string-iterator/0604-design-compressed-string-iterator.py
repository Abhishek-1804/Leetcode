from collections import deque

class StringIterator:
    def __init__(self, compressedString: str):
        self.queue = deque()
        n, i = len(compressedString), 0
        while i < n:
            char = compressedString[i]
            i += 1
            count = 0
            while i < n and compressedString[i].isdigit():
                count = count * 10 + int(compressedString[i])
                i += 1
            self.queue.append([char, count])

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        char, count = self.queue[0]
        self.queue[0][1] -= 1
        if self.queue[0][1] == 0:
            self.queue.popleft()
        return char

    def hasNext(self) -> bool:
        return len(self.queue) > 0
