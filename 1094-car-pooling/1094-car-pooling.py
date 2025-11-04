from collections import deque
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])  # sort by start time
        q = deque([])
        total_people = 0
        for people, start, end in trips:
            while q and start >= q[0][1]:
                total_people -= q.popleft()[0]
            if people + total_people > capacity:
                return False
            total_people += people
            q.append((people, end))
        return True
