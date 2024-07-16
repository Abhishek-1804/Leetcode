class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if target == nums[start]:
                break
            
            elif target > nums[mid]:
                start = mid + 1
            
            elif target <= nums[mid]:
                end = mid - 1

        if start >= len(nums) or nums[start] != target:
            return [-1, -1]

        start_ans = start
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if target == nums[end]:
                break
            
            elif target >= nums[mid]:
                start = mid + 1
            
            elif target < nums[mid]:
                end = mid - 1
        
        return [start_ans, end]