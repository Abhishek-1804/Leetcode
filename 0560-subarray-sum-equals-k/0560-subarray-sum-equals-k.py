class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum = 0
        sum_count = collections.defaultdict(int)
        sum_count[0] = 1  # Initialize with 0 sum occurring once
        ans = 0

        for num in nums:
            cum_sum += num

            # Check if there is a subarray (ending at the current index) that sums to k
            if (cum_sum - k) in sum_count:
                ans += 1
            
            # Update the count of the current cumulative sum
            sum_count[cum_sum] += 1
        
        return ans
