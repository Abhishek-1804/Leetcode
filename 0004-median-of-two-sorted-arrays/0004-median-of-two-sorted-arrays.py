class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

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