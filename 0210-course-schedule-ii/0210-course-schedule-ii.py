class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Initialize adjacency list to map each course to its dependent courses
        adj_list = {i: [] for i in range(numCourses)}
        
        # Populate adjacency list with dependencies
        for crs, pre in prerequisites:
            adj_list[pre].append(crs)
        
        # Initialize indegree array to count prerequisites for each course
        indegree = [0] * numCourses
        
        # Update indegree based on adjacency list
        for neighbors in adj_list.values():
            for neighbor in neighbors:
                indegree[neighbor] += 1

        print(indegree)
        print(adj_list)

        q = deque([])
        output = []

        for numOfPre in range(len(indegree)):
            if indegree[numOfPre] == 0:
                q.append(numOfPre)
        
        while q:
            pre = q.popleft()
            output.append(pre)

            for crs in adj_list[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:  # Add to queue only if no prerequisites remain
                    q.append(crs)

        return output if len(output) == numCourses else []