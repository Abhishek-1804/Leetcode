class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        regex_pattern = p.replace('*', '.*')
        
        return bool(re.search(regex_pattern, s))