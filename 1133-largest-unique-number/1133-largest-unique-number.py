class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        nums.sort(reverse = True)
        n = len(nums)

        if n == 1:
            return nums[0]
        
        pointer = 0
        while pointer < n:
            if pointer == n-1 or nums[pointer] != nums[pointer+1]:
                return nums[pointer]
            
            while pointer < n-1 and nums[pointer] == nums[pointer+1]:
                pointer += 1
            
            pointer += 1
        
        return -1
