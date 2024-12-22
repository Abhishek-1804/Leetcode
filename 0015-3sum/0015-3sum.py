class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            start = i+1
            end = len(nums)-1

            while start < end:
                total_sum = nums[start] + nums[end] + nums[i] 
                if total_sum == 0:
                    output.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    
                    while end > start and nums[end] == nums[end+1]:
                        end -= 1
                
                elif total_sum < 0:
                    start += 1
                
                else:
                    end -= 1
        
        return output