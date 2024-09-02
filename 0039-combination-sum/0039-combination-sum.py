class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        output = []
        temp = []

        def backtrack(t, start):
            if t == target:
                output.append(temp[:])
                return
            
            for c in range(start, len(candidates)):
                if t + candidates[c] <= target:
                    temp.append(candidates[c])
                    backtrack(temp, t+candidates[c], c)
                    temp.pop()
        
        backtrack(0, 0)
        return output