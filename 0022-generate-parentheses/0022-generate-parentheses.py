class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []


        def backtrack(temp_str, o, c):
            if o == 0 and c == 0:
                output.append(temp_str)
                return
            
            if o > 0:
                backtrack(temp_str + '(', o-1, c)
                
            if c > 0 and o < c:
                backtrack(temp_str + ')', o, c-1)


        backtrack("", n, n)

        return output