class Solution:
    def minMeetingRooms(self, intervals):
        import heapq
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        heap = []
        
        for interval in intervals:
            # If the earliest ending meeting is done before this meeting starts, reuse the room.
            if heap and heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        
        return len(heap)
