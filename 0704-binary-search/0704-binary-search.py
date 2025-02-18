class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end -= 1
            else:
                start += 1
        
        return -1