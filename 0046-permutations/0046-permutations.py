class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        output = []

        def backtrack(temp):
            if len(temp) == len(nums):
                output.append(temp[:])
                return
            
            for i in nums:
                if i in temp:
                    continue
                temp.append(i)
                backtrack(temp)
                temp.pop()
        
        backtrack([])
        return output
