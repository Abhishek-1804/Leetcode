class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        h = Counter(nums)
        operations = 0

        while len(h) != len(nums):
            for i in range(min(3, len(nums))):
                h[nums[0]] -= 1
                if h[nums[0]] == 0:
                    del h[nums[0]]
                nums.pop(0)
            operations += 1

        return operations