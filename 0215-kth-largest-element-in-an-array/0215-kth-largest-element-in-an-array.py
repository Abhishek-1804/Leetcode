class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)
        largest = heapq.nlargest(k, nums)
        return largest.pop()

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