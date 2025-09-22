class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        remove_start, remove_end = toBeRemoved
        
        for interval_start, interval_end in intervals:
            # Case 1: No overlap - interval is completely before or after removal interval
            if interval_start >= remove_end or interval_end <= remove_start:
                result.append([interval_start, interval_end])
            else:
                # Case 2: Overlap exists - keep non-overlapping parts
                
                # Keep left part if it exists (before removal starts)
                if interval_start < remove_start:
                    result.append([interval_start, remove_start])
                
                # Keep right part if it exists (after removal ends)
                if interval_end > remove_end:
                    result.append([remove_end, interval_end])
        
        return result
