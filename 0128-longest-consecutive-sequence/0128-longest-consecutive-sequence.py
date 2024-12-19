class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        h = {}
        max_num = 0

        for num in nums:
            if num not in h:
                left_length = h.get(num-1, 0)
                right_length = h.get(num+1, 0)
                curr_length = left_length + right_length + 1
                h[num+right_length] = curr_length
                h[num-left_length] = curr_length
                h[num] = curr_length
                max_num = max(max_num, curr_length)
        
        return max_num