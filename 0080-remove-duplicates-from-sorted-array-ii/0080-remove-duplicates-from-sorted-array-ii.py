class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        valid = 2

        for i in range(2, len(nums)):

            if nums[i] != nums[valid-2]:
                nums[valid] = nums[i]
                valid += 1
        
        return valid