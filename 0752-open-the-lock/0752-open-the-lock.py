class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        
        start = "0000"
        if start in deadends:
            return -1
            
        seen = set(deadends)
        q = deque([(start, 0)])
        
        while q:
            pos, turns = q.popleft()
            if pos == target:
                return turns
            if pos in seen:
                continue
            seen.add(pos)
            
            for i in range(4):
                digit = int(pos[i])
                # Forward rotation
                new_digit = (digit + 1) % 10
                new_pos = pos[:i] + str(new_digit) + pos[i+1:]
                q.append((new_pos, turns + 1))
                
                # Backward rotation
                new_digit = (digit - 1) % 10
                new_pos = pos[:i] + str(new_digit) + pos[i+1:]
                q.append((new_pos, turns + 1))
        
        return -1
