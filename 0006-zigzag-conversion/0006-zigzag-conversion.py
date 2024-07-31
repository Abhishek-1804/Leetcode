class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        i = 0
        ans = ''
        inc = 1
        temp_ans = [[""] for _ in range(numRows)]

        for char in s:
            temp_ans[i].append(char)
            i += inc
            
            if i == numRows-1:
                inc = -1
            if i == 0:
                inc = 1
        
        for i in range(len(temp_ans)):
            for j in range(len(temp_ans[i])):
                ans += temp_ans[i][j]
        
        return ans

        # if numRows == 1:
        #     return s
        
        # res = ''

        # for r in range(numRows):
        #     inc = (numRows-1) * 2

        #     for i in range(r, len(s), inc):
        #         res += s[i]
        #         if (r > 0 and r < numRows - 1 and i + inc - 2 * r < len(s)):
        #             res += s[i + inc-2*r]

        # return res