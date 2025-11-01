class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        h = {}
        answer = 0
        start = 0
        for end in range(n):
            h[s[end]] = h.get(s[end], 0) + 1
            window_len = end - start + 1
            most_freq_val = max(h.values())
            if window_len - most_freq_val <= k:
                answer = max(answer, window_len)
            else:
                h[s[start]] -= 1
                start += 1
        return answer