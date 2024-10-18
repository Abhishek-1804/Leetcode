class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i-1]

    def pickIndex(self) -> int:
        import random
        randNum = random.randint(1, self.w[-1])
        
        start, end = 0, len(self.w)-1
        while start < end:
            mid = (start+end) // 2
            if self.w[mid] == randNum:
                return mid
            elif self.w[mid] < randNum:
                start = mid + 1
            else:
                end = mid - 1
        
        return start

        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()