class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        def helper(m, n):
            if m == 0: return [""]
            if m == 1: return ["0", "1", "8"]
            prev = helper(m-2, n)
            res = []
            for mid in prev:
                if m != n:
                    res.append("0" + mid + "0")
                res.append("1" + mid + "1")
                res.append("6" + mid + "9")
                res.append("8" + mid + "8")
                res.append("9" + mid + "6")
            return res
            
        return helper(n, n)