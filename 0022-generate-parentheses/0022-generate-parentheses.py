class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []

        def backtrack(o, c, temp_str):
            if o == 0 and c == 0:
                output.append(temp_str)
                return
            
            if o > 0:
                backtrack(o-1, c, temp_str + '(')
            
            if c > o:
                backtrack(o, c-1, temp_str + ')')


        backtrack(n, n, '')

        return output