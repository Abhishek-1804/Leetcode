class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        output = []

        def backtrack(start, temp_arr):
            output.append(temp_arr[:])
            
            for i in range(start, len(nums)):
                temp_arr.append(nums[i])
                backtrack(i+1, temp_arr)
                temp_arr.pop()
        
        backtrack(0, [])
        return output