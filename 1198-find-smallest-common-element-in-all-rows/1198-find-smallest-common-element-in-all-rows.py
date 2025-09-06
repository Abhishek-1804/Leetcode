class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        intersect = set(mat[0])
        for i in range(1,len(mat)):
            set2 = set(mat[i])
            intersect = set2 & intersect
        return min(intersect) if intersect else -1
