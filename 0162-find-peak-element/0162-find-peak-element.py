class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        n = len(nums)
        start = 0
        end = n - 1

        while start <= end:
            mid = (start + end) // 2

            if mid == 0 and mid == n - 1:
                return mid
            
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    start = mid + 1
            
            elif mid == n - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    end = mid - 1
            
            # Middle case
            else:
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[mid - 1] > nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
