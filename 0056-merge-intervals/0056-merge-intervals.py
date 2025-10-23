class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]

        for i in intervals[1:]:
            if output[-1][-1] >= i[0]:
                output[-1][0] = min(output[-1][0], i[0])
                output[-1][-1] = max(output[-1][-1], i[1])
            else:
                output.append(i)
        
        return output