from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # Move the key to the end to show that it was recently used
            value = self.cache.pop(key)
            self.cache[key] = value  # reinsert item to move it to the end
            return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove existing key before reinserting it
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # popitem(last=False) pops the first item inserted if last is False
            self.cache.popitem(last=False)
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
