class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix = {0:1}
        ans = 0

        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum - k in prefix:
                ans += prefix[curr_sum - k]

            if curr_sum not in prefix:
                prefix[curr_sum] = 1
            else:
                prefix[curr_sum] += 1
            
        return ans