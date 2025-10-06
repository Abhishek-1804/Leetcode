class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        output = [-1, -1]

        if not nums:
            return output

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if target > nums[mid]:
                start = mid + 1
            
            else:
                end = mid - 1
        
        if end+1 < len(nums) and nums[end+1] == target:
            output[0] = end + 1

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if target < nums[mid]:
                end = mid - 1
            
            else:
                start = mid + 1
        
        if nums[start-1] == target:
            output[1] = start - 1

        return output