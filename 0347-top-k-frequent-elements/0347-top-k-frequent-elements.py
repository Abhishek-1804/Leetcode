class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)

        minHeap = [[-cnt, num] for num, cnt in counts.items()]
        heapq.heapify(minHeap)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(minHeap)[1])
        
        return ans