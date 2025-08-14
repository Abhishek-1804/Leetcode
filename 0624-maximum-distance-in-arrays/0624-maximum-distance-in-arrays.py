class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        min_val, max_val, answer = arrays[0][0], arrays[0][-1], float('-inf')

        for arr in arrays[1:]:
            answer = max(answer, max(abs(min_val - arr[-1]), abs(arr[0] - max_val)))
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])

        return answer
