class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)
        minLen = float('inf')
        left = 0
        curr_sum = 0
        flag = False

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                flag = True
                minLen = min(minLen, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if minLen == float('inf') else minLen