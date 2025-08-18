class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        n = len(s)
        reverse(0, n - 1)  # reverse the whole list first

        start = 0
        for end in range(n + 1):
            if end == n or s[end] == ' ':
                reverse(start, end - 1)
                start = end + 1