class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start + end) // 2
            mid_number = nums[mid]

            if target == mid_number:
                return mid
            elif target < mid_number:
                end -= 1
            else:
                start += 1
        
        return -1