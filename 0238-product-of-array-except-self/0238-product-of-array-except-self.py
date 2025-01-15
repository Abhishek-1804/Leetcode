class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        curr_prod = 1
        ans = []

        for i in nums:
            ans.append(curr_prod)
            curr_prod *= i
        
        print(ans)

        curr_prod = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= curr_prod
            curr_prod *= nums[i]
        
        return ans