class Solution:
    # bfs
    def findOrder_1(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        pre_to_crs = {i:[] for i in range(numCourses)}
        dependencies = [0] * numCourses

        for crs, pre in prerequisites:
            pre_to_crs[pre].append(crs)
            dependencies[crs] += 1

        q = deque([i for i in range(numCourses) if dependencies[i] == 0])
        result = []

        while q:
            crs = q.popleft()
            result.append(crs)

            for neighbor in pre_to_crs[crs]:
                dependencies[neighbor] -= 1
                if dependencies[neighbor] == 0:
                    q.append(neighbor)
        
        return result if len(result) == numCourses else []

    # dfs
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        crs_to_pre = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            crs_to_pre[crs].append(pre)
        
        # 0 - not visited
        # 1 - currently visiting
        # 2 - visited
        states = [0]*numCourses
        result = []

        def has_cycle(i):
            if states[i] == 1:
                return True
            if states[i] == 2:
                return False

            states[i] = 1
            for crs in crs_to_pre[i]:
                if has_cycle(crs):
                    return True
            states[i] = 2

            result.append(i)
            return False

        for i in range(numCourses):
            if states[i] == 0:
                if has_cycle(i):
                    return []

        return result