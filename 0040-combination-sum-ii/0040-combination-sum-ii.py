class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        output = []
        
        def backtrack(temp_list, curr_sum, start):
            if curr_sum == target:
                output.append(temp_list[:])
                return
            
            for c in range(start, len(candidates)):
                if c > start and candidates[c] == candidates[c-1]:
                    continue

                if curr_sum + candidates[c] <= target:
                    backtrack(temp_list + [candidates[c]], curr_sum + candidates[c], c+1)
         
        backtrack([], 0, 0)
        return output