class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []

        o = c = n

        def dfs(o, c, s):

            if o == 0 and c == 0:
                output.append(s)
                return
            
            if o > 0:
                dfs(o-1, c, s+'(')
            
            if c > o:
                dfs(o, c-1, s+')')

        dfs(o, c, "")
        return output