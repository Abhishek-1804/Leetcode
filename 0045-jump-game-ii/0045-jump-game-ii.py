class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return 0
        
        end = 0
        jump = 0
        farthest = 0

        for i in range(len(nums)):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums)-1:
                return jump + 1
            if i == end:
                jump += 1
                end = farthest
        
        return jump