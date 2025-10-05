class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []

        def backtrack(total, temp_list, start):
            if total == target:
                output.append(temp_list[:])
                return
            
            for i in range(start, len(candidates)):
                total += candidates[i]
                if total <= target:
                    temp_list.append(candidates[i])
                    backtrack(total, temp_list, i)
                    temp_list.pop()
                total -= candidates[i]

        backtrack(0, [], 0)
        return output