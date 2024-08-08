class RandomizedSet:

    def __init__(self):
        self.seen = set()
        self.count = 0

    def insert(self, val: int) -> bool:
        if val in self.seen:
            return False
        self.seen.add(val)
        self.count += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.seen:
            return False
        self.seen.remove(val) 
        self.count -= 1
        return True

    def getRandom(self) -> int:
        r = random.randint(0, self.count-1)
        return list(self.seen)[r]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()