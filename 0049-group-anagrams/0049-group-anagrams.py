class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in h:
                h[sorted_word] = []
            h[sorted_word].append(word)
        
        ans = []

        for key, val in h.items():
            ans.append(val)
        
        return ans