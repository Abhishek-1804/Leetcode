class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        
        total_sum = sum(nums)
        counts = Counter(nums)
        outlier = float('-inf')
        
        for num in nums:
            counts[num] -= 1
            total_sum -= num

            if total_sum % 2 == 0 and counts[total_sum // 2] > 0:
                outlier = max(outlier, num)
            
            counts[num] += 1
            total_sum += num
        
        return outlier