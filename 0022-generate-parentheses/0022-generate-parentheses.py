class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []

        def dfs(open, closed, s):
            if open == closed == n:
                output.append(s)
                return
            
            if open < n:
                dfs(open+1, closed, s + '(')
            
            if closed < open:
                dfs(open, closed+1, s + ')')

        dfs(0, 0, "")
        return output
