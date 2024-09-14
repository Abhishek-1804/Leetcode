class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        ans = []
        prefix = [arr[0]]
        temp = arr[0]
        
        for num in arr[1:]:
            temp ^= num
            prefix.append(temp)
        
        for left, right in queries:
            if left == 0:
                ans.append(prefix[right])
            else:
                ans.append(prefix[right] ^ prefix[left-1])
        
        return ans
