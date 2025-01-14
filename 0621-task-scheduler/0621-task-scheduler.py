class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        max_freq = max(count.values())
        max_count = sum(1 for freq in count.values() if freq == max_freq)

        # The core formula:
        # max_freq-1 * (n+1) is giving us the block structure
        # so we add max_count again once in the end because the rest of the slots are covered by smaller freq tasks

        intervals = (max_freq - 1) * (n + 1) + max_count

        # The result can't be smaller than the total number of tasks
        return max(intervals, len(tasks))

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