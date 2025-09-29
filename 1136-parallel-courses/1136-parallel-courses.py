class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        from collections import defaultdict
        
        graph = defaultdict(list)
        for pre, course in relations:
            graph[pre].append(course)
        
        memo = {}
        visiting = set()
        
        def dfs(course):
            if course in memo:
                return memo[course]
            if course in visiting:
                return -1  # cycle detected
            visiting.add(course)
            max_len = 1
            for next_course in graph[course]:
                res = dfs(next_course)
                if res == -1:
                    return -1
                max_len = max(max_len, 1 + res)
            visiting.remove(course)
            memo[course] = max_len
            return max_len
        
        res = 0
        for i in range(1, n+1):
            path_len = dfs(i)
            if path_len == -1:
                return -1
            res = max(res, path_len)
        return res
