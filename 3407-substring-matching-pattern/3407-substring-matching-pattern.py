class Solution:
    def hasMatch(self, s: str, p: str) -> bool:

        left_part, right_part = p.split('*')

        left_index = s.find(left_part)
        right_index = s.find(right_part, left_index + len(left_part))

        return left_index != -1 and right_index != -1