class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        n = len(nums)
        l, r = 0, n

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        leftmost = l

        l, r = 0, n

        while l < r:
            mid = (l + r) // 2

            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        
        rightmost = l

        return (rightmost - leftmost) > n / 2