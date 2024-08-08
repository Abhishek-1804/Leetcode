class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        ans = []
        
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    if (nums[i], nums[j], nums[k]) not in seen:
                        ans.append([nums[i], nums[j], nums[k]])
                        seen.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        
        return ans