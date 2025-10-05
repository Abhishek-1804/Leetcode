class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []

        def backtrack(temp_list):
            if len(temp_list) == len(nums):
                output.append(temp_list[:])
                return
            
            for i in nums:
                if i in temp_list:
                    continue
                temp_list.append(i)
                backtrack(temp_list)
                temp_list.pop()


        backtrack([])
        return output