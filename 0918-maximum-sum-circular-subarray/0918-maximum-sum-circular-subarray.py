class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        max_sum = float('-inf')
        min_sum = float('inf')
        curr_max = nums[0]
        curr_min = nums[0]

        for i in nums[1:]:
            curr_max = max(curr_max + i, i)
            curr_min = min(curr_min + i, i)
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)

        return max_sum if max_sum < 0 else max(max_sum, sum(nums) - min_sum)