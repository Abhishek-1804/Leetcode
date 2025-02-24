class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0
        prefix_map = {0: 1}
        temp_sum = 0
        
        for num in nums:
            temp_sum += num
            # Check if there is a prefix sum that when removed from temp_sum equals k
            if temp_sum - k in prefix_map:
                output += prefix_map[temp_sum - k]
            # Update the count of temp_sum in the map
            prefix_map[temp_sum] = prefix_map.get(temp_sum, 0) + 1
        
        return output