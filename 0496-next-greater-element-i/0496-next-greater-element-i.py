class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        n = len(nums1)
        m = len(nums2)

        for i in range(n):
            flag = True
            for j in range(nums2.index(nums1[i]), m):
                if nums2[j] > nums1[i]:
                    flag = False
                    ans.append(nums2[j])
                    break
            
            if flag:
                ans.append(-1)

            
        return ans