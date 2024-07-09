class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []

        def dfs(temp, start):
            if len(temp) == k:
                ans.append(temp.copy())
                return
            
            for i in range(start, n+1):
                temp.append(i)
                dfs(temp, i+1)
                temp.pop()

        dfs([], 1)
        return ans

