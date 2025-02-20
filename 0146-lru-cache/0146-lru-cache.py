class Doubly:
    def __init__(self, k, v, next=None, prev=None):
        self.k = k
        self.v = v
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.h = {}

        self.head = Doubly(0, 0)
        self.tail = Doubly(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.h:
            return -1

        node = self.h[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

        return node.v
        
    def put(self, key: int, value: int) -> None:
        if key in self.h:
            node = self.h[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.prev.next = node
            node.prev = self.tail.prev
            self.tail.prev = node
            node.next = self.tail
            node.v = value

        else:
            if self.count == self.capacity:
                node = self.head.next
                node.prev.next = node.next
                node.next.prev = node.prev
                del self.h[node.k]
                self.count -= 1

            node = Doubly(key, value)
            self.h[key] = node
            self.tail.prev.next = node
            node.prev = self.tail.prev
            self.tail.prev = node
            node.next = self.tail
            node.v = value
            self.count += 1
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)