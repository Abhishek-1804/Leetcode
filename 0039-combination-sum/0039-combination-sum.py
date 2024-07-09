class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        temp = []

        def dfs(idx, sum_):

            if sum_ == target:
                output.append(temp.copy())
            
            elif sum_ < target:
                for j in range(idx, len(candidates)):
                    temp.append(candidates[j])
                    dfs(j, sum_ + candidates[j])
                    temp.pop()

        dfs(0, 0)
        return output