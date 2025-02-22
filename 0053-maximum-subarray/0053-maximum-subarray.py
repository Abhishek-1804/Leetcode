class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        output = float('-inf')
        temp_sum = 0

        for num in nums:
            temp_sum += num
            if num > temp_sum:
                temp_sum = num
            
            output = max(output, temp_sum)
        
        return output