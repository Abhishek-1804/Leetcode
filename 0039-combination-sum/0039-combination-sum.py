class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []

        def backtrack(start, temp_arr, temp_sum):
            if temp_sum > target:
                return

            if temp_sum == target:
                output.append(temp_arr[:])
                return
            
            for j in range(start, len(candidates)):
                temp_arr.append(candidates[j])
                backtrack(j, temp_arr, temp_sum + candidates[j])
                temp_arr.pop()

        # iterator for candidates, temp_arr, temp_sum
        backtrack(0, [], 0)
        return output