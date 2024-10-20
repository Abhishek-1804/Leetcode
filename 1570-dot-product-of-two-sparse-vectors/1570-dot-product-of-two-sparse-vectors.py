class SparseVector:
    def __init__(self, nums: List[int]):
        self.arr = []

        for i, num in enumerate(nums):
            if num != 0:
                self.arr.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i = j = 0
        ans = 0
        
        while i < len(self.arr) and j < len(vec.arr):
            i_idx, i_val = self.arr[i]
            j_idx, j_val = vec.arr[j]

            if i_idx == j_idx:
                ans += i_val*j_val
                i += 1
                j += 1
            
            elif i_idx < j_idx:
                i += 1
            
            else:
                j += 1
        
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)