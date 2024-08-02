class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) <= 1:
            return True

        farthest = 0

        for i in range(len(nums)):
            farthest = max(farthest, nums[i] + i)
            if farthest >= len(nums)-1:
                return True
                
            if i == farthest:
                return False
        
        return True