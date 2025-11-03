class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        furthest = 0
        current_end = 0
        jumps = 0

        for end in range(n-1):
            furthest = max(furthest, nums[end] + end)

            if end == current_end:
                jumps += 1
                current_end = furthest
        
        return jumps