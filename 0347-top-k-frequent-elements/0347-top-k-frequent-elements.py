class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_count = Counter(nums)
        maxHeap = [[-cnt, char] for char, cnt in nums_count.items()]
        heapq.heapify(maxHeap)

        result = []

        for _ in range(k):
            result.append(heapq.heappop(maxHeap)[1])
        
        return result