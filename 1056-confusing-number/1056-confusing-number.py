class Solution:
    def confusingNumber(self, n: int) -> bool:

        rotate_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        rotated = []
        for c in reversed(str(n)):
            if c not in rotate_map:
                return False
            rotated.append(rotate_map[c])
        return ''.join(rotated) != str(n)