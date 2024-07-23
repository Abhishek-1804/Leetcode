class Solution:
    def coinChange(self, arr: List[int], sum_: int) -> int:
        
        d = [[-1 for i in range(sum_ + 1)] for j in range(len(arr) + 1)]

        for i in range(len(d[0])):
            d[0][i] = float('inf')

        for i in range(1, len(d)):
            d[i][0] = 0

        for i in range(1, len(d[0])):
            if i % arr[0] == 0:
                d[1][i] = i // arr[0]

            else:
                d[1][i] = float('inf')

        for i in range(2, len(d)):
            for j in range(1, len(d[0])):

                if j >= arr[i-1]:
                    d[i][j] = min(d[i][j-arr[i-1]] + 1, d[i-1][j])

                else:
                    d[i][j] = d[i-1][j]

        return -1 if d[-1][-1] == float('inf') else d[-1][-1]