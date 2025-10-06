class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                output.append(path[:])
                return
            for end in range(start, len(s)):
                if is_palindrome(s[start:end+1]):
                    backtrack(end+1, path + [s[start:end+1]])

        backtrack(0, [])
        return output
