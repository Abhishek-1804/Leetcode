class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        ans = []
        cache = {}

        for left, right in queries:
            if (left, right) in cache:
                ans.append(cache[(left, right)])
            else:
                temp_ans = arr[left]
                for ele in range(left+1, right+1, 1):
                    temp_ans ^= arr[ele]
                cache[(left, right)] = temp_ans
                ans.append(temp_ans)
        
        return ans