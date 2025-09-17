class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
        for r in range(len(mat1)):
            for c in range(len(mat2[0])):
                temp = 0
                for i in range(len(mat1[0])):
                    temp += mat1[r][i] * mat2[i][c]
                res[r][c] = temp
        return res