class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        zero = 0
        for num in nums:
            if num == zero:
                zero = 1
                break

        return len(set(nums)) - zero