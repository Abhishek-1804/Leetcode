from typing import List
import math

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        output = []

        def backtrack(start, remaining, ans):
            if ans and remaining >= start:
                output.append(ans + [remaining])
            
            # if we go beyond sqrt(n), we start repeating values
            for i in range(start, int(math.sqrt(remaining)) + 1):
                if remaining % i == 0:
                    backtrack(i, remaining // i, ans + [i])

        backtrack(2, n, [])
        return output
