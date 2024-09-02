class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        output = []
        temp = []

        def backtrack():
            if len(temp) == len(nums):
                output.append(temp[:])
                return
            
            for i in nums:
                if i in temp:
                    continue
                temp.append(i)
                backtrack()
                temp.pop()
        
        backtrack()
        return output
