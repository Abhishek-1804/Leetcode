class Solution:
    def jump(self, nums: List[int]) -> int:

        # # sol 1
        # result = 0
        # l = r = 0

        # while r < len(nums) - 1:
        #     furthest = 0

        #     for i in range(l, r+1):
        #         furthest = max(furthest, nums[i] + i)
            
        #     l = r+1
        #     r = furthest
        #     result += 1

        # return result

        # sol 2
        result = 0
        end = 0
        farthest = 0

        if len(nums) == 1:
            return 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            if farthest >= len(nums) - 1:
                return result + 1
            if i == end:
                result += 1
                end = farthest
            