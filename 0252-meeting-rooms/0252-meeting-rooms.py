class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if not intervals:
            return True

       intervals.sort(key = lambda x: x[0]) 

       prev = intervals[0][1]

       for i in intervals[1:]:
        if prev > i[0]:
            return False
        prev = i[1]

        return True