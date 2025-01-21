class Solution:
    def reorganizeString(self, s: str) -> str:
        
        s_count = Counter(s)

        maxHeap = [[-cnt, char] for char, cnt in s_count.items()]
        heapq.heapify(maxHeap)

        prev = None
        ans = ""

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            cnt += 1
            ans += char

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
        
        return ans