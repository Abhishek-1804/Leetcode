class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:

        n = len(s)
        bold_flags = [False] * n

        for substring in words:
            start = 0
            while True:
                pos = s.find(substring, start)
                if pos == -1:
                    break
                # Mark characters from pos to pos + len(word) as bold
                for i in range(pos, pos + len(substring)):
                    bold_flags[i] = True
                start = pos + 1  # Move to next position to find overlapping match
        
        # Build result string with bold tags
        result = []
        for i in range(n):
            # Add opening tag if current char should be bold and previous wasn't
            if bold_flags[i] and (i == 0 or not bold_flags[i-1]):
                result.append("<b>")
            
            result.append(s[i])
            
            # Add closing tag if current char should be bold and next char shouldn't be
            if bold_flags[i] and (i == n-1 or not bold_flags[i+1]):
                result.append("</b>")
        
        return "".join(result)