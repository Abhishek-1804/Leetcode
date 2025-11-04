class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # return self.findMedianSortedArrays_merging(nums1, nums2)
        return self.findMedianSortedArrays_binary_search(nums1, nums2)

    def findMedianSortedArrays_binary_search(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if i+1 < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if j+1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


    def findMedianSortedArrays_merging(self, nums1: List[int], nums2: List[int]) -> float:

        merged_array = []
        m, n = len(nums1), len(nums2)
        n1, n2 = 0, 0

        while n1 < m and n2 < n:
            if nums1[n1] < nums2[n2]:
                merged_array.append(nums1[n1])
                n1 += 1
            else:
                merged_array.append(nums2[n2])
                n2 += 1
        
        while n1 < m:
            merged_array.append(nums1[n1])
            n1 += 1

        while n2 < n:
            merged_array.append(nums2[n2])
            n2 += 1
        
        mid = (m+n) // 2
        if (m + n) % 2 == 1:
            return merged_array[mid]
        else:
            return (merged_array[mid-1] + merged_array[mid]) / 2