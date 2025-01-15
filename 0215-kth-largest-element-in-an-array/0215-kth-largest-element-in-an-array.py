class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap = [-i for i in nums]
        heapq.heapify(maxHeap)

        for _ in range(k-1):
            heapq.heappop(maxHeap)
        
        return -heapq.heappop(maxHeap)