class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        prefix_counts = {0: 1}  # empty prefix sum base case

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in prefix_counts:
                count += prefix_counts[prefix_sum - k]
            prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1
        return count
