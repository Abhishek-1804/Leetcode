class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        max_len = 0
        num_zeros = 0
        n = len(nums)
        l = 0

        for r in range(n):
            if nums[r] == 0:
                num_zeros += 1
            
            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len