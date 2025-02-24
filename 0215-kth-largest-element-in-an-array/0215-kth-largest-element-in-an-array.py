class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap = list(map(lambda x: -x, nums))
        heapq.heapify(maxHeap)

        for _ in range(k-1):
            heapq.heappop(maxHeap)
        
        return -heapq.heappop(maxHeap)
