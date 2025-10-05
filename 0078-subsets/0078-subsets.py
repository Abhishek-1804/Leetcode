class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        n = len(nums)

        def backtrack(temp_list, start):
            output.append(temp_list[:])
            
            for i in range(start, n):
                temp_list.append(nums[i])
                backtrack(temp_list, i + 1)
                temp_list.pop()

        backtrack([], 0)
        return output