class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        num_counts = {}

        for num in nums:
            if num not in num_counts:
                num_counts[num] = 1
            else:
                num_counts[num] += 1
        
        filtered_d = [k for k, v in num_counts.items() if v == 1]
        return max(filtered_d) if filtered_d else -1