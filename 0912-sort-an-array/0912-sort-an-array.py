from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Base case: if the array has 1 or 0 elements, it is already sorted
        if len(nums) <= 1:
            return nums
        
        # Recursive division of the array into left and right halves
        mid = len(nums) // 2
        left_sorted = self.sortArray(nums[:mid])
        right_sorted = self.sortArray(nums[mid:])
        
        # Merge the two sorted halves and return
        return self.merge(left_sorted, right_sorted)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        output = []
        l, r = 0, 0
        
        # Merge elements from left and right in sorted order
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                output.append(left[l])
                l += 1
            else:
                output.append(right[r])
                r += 1
                
        # Append remaining elements from left (if any)
        while l < len(left):
            output.append(left[l])
            l += 1
            
        # Append remaining elements from right (if any)
        while r < len(right):
            output.append(right[r])
            r += 1
            
        return output
