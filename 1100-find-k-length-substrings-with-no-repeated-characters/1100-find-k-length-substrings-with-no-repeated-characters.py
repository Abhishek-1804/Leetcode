class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        answer = 0
        left = 0
        char_set = set()

        for right in range(n):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            if right - left + 1 == k:
                answer += 1
                char_set.remove(s[left])
                left += 1
        return answer
