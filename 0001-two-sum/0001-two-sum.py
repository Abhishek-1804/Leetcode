class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hmap = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val not in hmap:
                hmap[nums[i]] = i
            else:
                return [hmap[val], i]