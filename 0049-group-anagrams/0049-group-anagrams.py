class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = {}

        for word in strs:
            if ''.join(sorted(word)) not in h:
                h[''.join(sorted(word)) ] = []
            h[''.join(sorted(word))].append(word)
        
        ans = []

        for key, val in h.items():
            ans.append(val)
        
        return ans