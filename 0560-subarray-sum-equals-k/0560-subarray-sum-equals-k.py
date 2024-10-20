class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum = 0
        sum_count = {0:1}
        ans = 0

        for num in nums:
            cum_sum += num

            # Check if there is a subarray (ending at the current index) that sums to k
            if (cum_sum - k) in sum_count:
                ans += sum_count[cum_sum - k]
            
            # Update the count of the current cumulative sum
            if cum_sum not in sum_count:
                sum_count[cum_sum] = 1
            else:
                sum_count[cum_sum] += 1
        
        return ans
