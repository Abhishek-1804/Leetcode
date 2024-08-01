class Solution:
    def jump(self, nums: List[int]) -> int:

        counter = 0
        
        if len(nums) == 1:
            return 0

        q = deque([(0, 0)])
        visited = set()

        while q:
            ind, count = q.popleft()
            if ind == len(nums)-1:
                return count
            
            if nums[ind] == 0:
                continue

            for j in range(1, nums[ind] + 1):
                jump = j + ind
                if jump < len(nums) and jump not in visited:
                    q.append((jump, count+1))
                    visited.add(jump)