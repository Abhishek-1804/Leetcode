class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        ans = []

        def dfs(temp_list, start):
            if len(temp_list) == k:
                ans.append(temp_list[:])
                return
            
            for i in range(start, n+1):
                temp_list.append(i)
                dfs(temp_list, i+1)
                temp_list.pop()
            
        dfs([], 1)
        return ans
