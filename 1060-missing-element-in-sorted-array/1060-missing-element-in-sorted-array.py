class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        return self.missingElement_binary_search(nums, k)
        # return self.missingElement_brute_force(nums, k)

    def missingElement_binary_search(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1

        missing = lambda x: nums[x] - nums[0] - x

        if k > missing(r):
            return nums[r] - missing(r) + k
        
        while l < r:
            mid = (l + r) // 2
            i = missing(mid)
            if k <= i:
                r = mid
            else:
                l = mid
        
        return nums[l] - missing(l) + k

    def missingElement_brute_force(self, nums: List[int], k: int) -> int:

        n = len(nums)
        for i in range(1, n):
            gap = nums[i] - nums[i-1] - 1
            if gap >= k:
                return nums[i-1] + k
            k -= gap
        return nums[-1] + k
