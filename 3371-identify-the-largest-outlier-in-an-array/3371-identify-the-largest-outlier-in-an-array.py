class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        
        pos = {num:i for i, num in enumerate(nums)}
        total = sum(nums)
        outlier = float('-inf')

        for i, num in enumerate(nums):
            if (total - num) % 2 == 0:
                if (total-num) // 2 in pos:
                    if i != pos[(total-num) // 2]:
                        outlier = max(outlier, num)
        
        return outlier
                    
