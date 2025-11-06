class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        h = {}
        answer = 0
        start = 0

        for end in range(len(s)):
            h[s[end]] = h.get(s[end], 0) + 1
            most_freq_val = max(h.values())
            window_length = end - start + 1
            if window_length - most_freq_val <= k:
                answer = max(answer, window_length)
            else:
                h[s[start]] -= 1
                start += 1
        
        return answer
