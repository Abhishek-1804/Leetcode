class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return 0

        farthest = 0
        jumps = 0
        end = 0

        for i in range(len(nums)):
            farthest = max(farthest, nums[i] + i)

            if farthest >= len(nums) - 1:
                return jumps + 1
            
            if i == end:
                jumps += 1
                end = farthest
        
        return jumps