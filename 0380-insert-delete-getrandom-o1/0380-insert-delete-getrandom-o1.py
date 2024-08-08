class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.arr.append(val)
            self.dict[val] = len(self.arr)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        [1, 2, 3, 4, 5]

        if val not in self.dict:
            return False
        
        idx = self.dict[val]
        self.arr[idx] = self.arr[-1]
        self.dict[self.arr[-1]] = idx
        self.arr.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()