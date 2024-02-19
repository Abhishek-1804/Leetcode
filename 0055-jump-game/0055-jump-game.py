class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # sol 1: going backward and checking if we can move 1 forward
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):

            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0

        # # sol 2
        # reachable = 0

        # for i in range(len(nums)):

        #     if reachable < i:
        #         return False
            
        #     reachable = max(reachable, i + nums[i])
        
        # return True