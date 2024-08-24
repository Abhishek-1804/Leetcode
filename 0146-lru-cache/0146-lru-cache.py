class Doubly:

    def __init__(self, k, val, prev = None, nxt = None):
        self.k = k
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}
        self.head = Doubly(0, 0)
        self.tail = Doubly(-1, -1)
        self.head.nxt = self.tail
        self.tail.prev = self.head        

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        node = self.hmap[key]
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        self.tail.prev.nxt = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.nxt = self.tail
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
            self.tail.prev.nxt = node
            node.prev = self.tail.prev
            self.tail.prev = node
            node.nxt = self.tail
        
        else:
            if len(self.hmap) == self.capacity:
                n = self.head.nxt
                self.head.nxt = n.nxt
                n.nxt.prev = self.head
                del self.hmap[n.k]
            node = Doubly(key, value)
            self.hmap[key] = node
            self.tail.prev.nxt = node
            node.prev = self.tail.prev
            self.tail.prev = node
            node.nxt = self.tail

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)