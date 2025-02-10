class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Dictionary to store the next greater element for each number in nums2
        next_greater = {}
        stack = []
        
        # Iterate over nums2 and build the next greater mapping
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # For any remaining elements in the stack, there is no next greater element.
        while stack:
            next_greater[stack.pop()] = -1
        
        # Build the result for nums1 using the precomputed mapping
        return [next_greater[num] for num in nums1]

    def nextGreaterElement_bf(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
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