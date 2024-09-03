class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        curr_min_sum = min_sum = curr_max_sum = max_sum = nums[0]
        total_sum = sum(nums)

        for num in nums[1:]:
            curr_min_sum = min(num, curr_min_sum + num)
            min_sum = min(min_sum, curr_min_sum)
            curr_max_sum = max(num, curr_max_sum + num)
            max_sum = max(max_sum, curr_max_sum)
        
        if max_sum < 0:
            return max_sum
        return max(max_sum, total_sum - min_sum)