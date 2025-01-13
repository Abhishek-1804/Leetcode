class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        max_freq = max(count.values())
        max_count = sum(1 for freq in count.values() if freq == max_freq)

        total_slots = n * (max_freq-1)
        idle_slots = total_slots - (max_count - 1)
        remaining_tasks = len(tasks) - (max_freq * max_count)
        remaining_slots = idle_slots - remaining_tasks

        if remaining_slots > 0:
            return len(tasks) + remaining_slots
        
        else:
            return len(tasks)

    def leastInterval_1(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque([])

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt += 1
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time