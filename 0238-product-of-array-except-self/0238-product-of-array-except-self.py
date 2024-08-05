class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        cur_prod = 1
        ans = []

        for i in range(len(nums)):
            ans.append(cur_prod)
            cur_prod *= nums[i]
        
        cur_prod = nums[-1]

        cur_prod = 1

        for i in range(len(nums)-1, -1, -1):
            ans[i] *= cur_prod
            cur_prod *= nums[i]
        
        return ans