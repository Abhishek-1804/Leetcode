class Solution:
    def reorganizeString(self, s: str) -> str:
        
        answer = ''
        freq = Counter(s)
        maxHeap = [[-count, c] for c, count in freq.items()]

        heapq.heapify(maxHeap)

        prev = None

        while maxHeap or prev:

            if not maxHeap and prev:
                return ''

            cnt, c = heapq.heappop(maxHeap)
            cnt += 1
            answer += c

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt < 0:
                prev = [cnt, c]
        
        return answer
            