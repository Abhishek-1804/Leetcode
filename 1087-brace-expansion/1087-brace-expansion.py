class Solution:
    def expand(self, s: str) -> List[str]:

        output = []

        def backtrack(ind, temp_str):
            if ind == len(s):
                output.append(temp_str)
                return
            
            if s[ind] == '{':
                end = s.index('}', ind)

                options = s[ind+1:end].split(',')

                for op in sorted(options):
                    backtrack(end + 1, temp_str+op)
            else:
                backtrack(ind+1, temp_str+s[ind])

        backtrack(0, "")

        return options
