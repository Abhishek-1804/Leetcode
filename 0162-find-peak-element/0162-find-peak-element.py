class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start+end) // 2

            if (mid == 0 and nums[mid] > nums[mid+1]) or (mid == len(nums)-1 and nums[mid] > nums[mid-1]):
                return mid

            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            
            elif nums[mid] > nums[mid+1]:
                end = mid-1
            
            else:
                start = mid+1