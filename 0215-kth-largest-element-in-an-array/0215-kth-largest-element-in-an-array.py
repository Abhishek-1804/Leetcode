class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def heapify_up(self, index):
        parent = (index-1) // 2
        
        if index > 0 and self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapify_up(parent)
    
    def heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.heapify_down(largest)
    
    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)
    
    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxHeap = MaxHeap()

        for i in nums:
            maxHeap.insert(i)
        
        for _ in range(k-1):
            maxHeap.extract_max()
        
        return maxHeap.extract_max()

        ## QuickSelect Solution (similar to quicksort; but fails for 1 test case)
        # k = len(nums) - k
 
        # def quickSelect(l, r):
            # pivot, pointer = nums[r], l
 
            # for i in range(l, r):
                # if nums[i] <= pivot:
                    # nums[i], nums[pointer] = nums[pointer], nums[i]
                    # pointer += 1
            # nums[pointer], nums[r] = nums[r], nums[pointer]
 
            # if pointer < k:
                # return quickSelect(pointer + 1, r)
             
            # elif pointer > k:
                # return quickSelect(l, pointer - 1)
             
            # else:
                # return nums[pointer]
         
        # return quickSelect(0, len(nums)-1)