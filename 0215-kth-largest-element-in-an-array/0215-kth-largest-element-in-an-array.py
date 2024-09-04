class MinHeap:
    def __init__(self):
        self.heap = []
    
    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def _heapify_up(self, index):
        parent = (index-1) // 2
        if index > 0 and parent >= 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)
    
    def _heap_insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap)-1)
    
    def _heap_pop(self):
        if not self.heap:
            return
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return root

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def _heapify_up(self, index):
        parent = (index-1) // 2
        if index > 0 and parent >= 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)
    
    def heap_insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap)-1)
    
    def heap_pop(self):
        if not self.heap:
            return
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return root

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = MaxHeap()
        for num in nums:
            h.heap_insert(num)

        for _ in range(k-1):
            h.heap_pop()
        
        return h.heap_pop()