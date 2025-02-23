class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        check = None
        pointer = 0

        for i in range(len(nums)):
            if nums[i] != check:
                nums[pointer] = nums[i]
                check = nums[i]
                pointer += 1
                
        return pointer