class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        answer = 0
        
        # Fix the largest side and iterate from end to start
        for k in range(n - 1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # All pairs (i, i+1, ..., j-1) with j form valid triangles
                    answer += j - i
                    j -= 1
                else:
                    i += 1
        
        return answer
