class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        diff = [0] * 1001

        for num_pass, start, end in trips:
            diff[start] += num_pass
            diff[end] -= num_pass

        passengers = 0

        for x in diff:
            passengers += x
            if passengers > capacity:
                return False
                
        return True
   