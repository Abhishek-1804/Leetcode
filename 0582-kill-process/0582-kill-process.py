class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        from collections import deque, defaultdict

        parent_to_child = defaultdict(list
        output = []

        for i in range(len(ppid)):
            parent_to_child[ppid[i]].append(pid[i])
        
        bfs_q = deque([kill])

        while bfs_q:
            parent = bfs_q.popleft()
            output.append(parent)
            if parent in parent_to_child:
                for child in parent_to_child[parent]:
                    bfs_q.append(child)
        
        return output