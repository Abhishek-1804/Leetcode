class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        answer = []

        for num in nums1:
            answer.append(nums2.index(num))
        
        return answer