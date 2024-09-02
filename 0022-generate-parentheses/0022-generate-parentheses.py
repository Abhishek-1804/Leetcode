class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []
        temp_str = ''

        def backtrack(opening, closing):
            nonlocal temp_str
            if opening == closing == n:
                output.append(temp_str)
                return
            
            if opening < n:
                temp_str += '('
                backtrack(opening+1, closing)
                temp_str = temp_str[:-1]
            if closing < opening:
                temp_str += ')'
                backtrack(opening, closing+1)
                temp_str = temp_str[:-1]

        backtrack(0, 0)
        return output