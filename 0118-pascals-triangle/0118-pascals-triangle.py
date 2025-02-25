class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = []

        if numRows < 1:
            return output
        
        output.append([1])

        for i in range(numRows-1):
            temp_arr = []

            if i == 0:
                output.append([1, 1])
            else:
                temp_arr.append(1)
                for j in range(1, len(output[-1])):
                    temp_arr.append(output[-1][j] + output[-1][j-1])
                temp_arr.append(1)
                output.append(temp_arr)
        
        return output