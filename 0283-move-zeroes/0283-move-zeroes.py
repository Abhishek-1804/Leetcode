class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            if nums[i] == 0:
                start = i+1
                while start < len(nums):
                    if nums[start] != 0:
                        nums[start], nums[i] = nums[i], nums[start]
                        break
                    start += 1
                if start == len(nums):
                    break
        