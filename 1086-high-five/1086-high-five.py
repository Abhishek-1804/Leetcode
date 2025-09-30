class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        from collections import defaultdict
        import heapq

        h = defaultdict(list)

        for i, score in items:
            heapq.heappush(h[i], score)
            if len(h[i]) > 5:
                heapq.heappop(h[i])
        
        output = []
        for student_id in sorted(h.keys()):
            avg = sum(h[student_id]) // 5
            output.append([student_id, avg])
        return output