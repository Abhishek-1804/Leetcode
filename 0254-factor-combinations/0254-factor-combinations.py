from typing import List

class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        output = []

        def backtrack(start, n, ans):
            # Add current combination if valid
            if ans and n >= start:
                output.append(ans + [n])
            
            # Continue exploring factors (not else - always explore!)
            i = start
            while i * i <= n:
                if n % i == 0:
                    backtrack(i, n // i, ans + [i])
                i += 1

        backtrack(2, n, [])
        return output
