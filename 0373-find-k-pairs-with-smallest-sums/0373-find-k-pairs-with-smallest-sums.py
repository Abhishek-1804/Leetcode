class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        min_heap = []
        
        for j in range(min(k, len(nums2))):
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))

        result = []

        while k > 0 and min_heap:
            sum_, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1
            if i + 1 < len(nums1):
                # Push the next element in nums1 with the current element in nums2
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))

        return result