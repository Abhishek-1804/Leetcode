class Doubly:
    def __init__(self, k = -1, v = -1, next = None, prev = None):
        self.k = k
        self.v = v
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Doubly()
        self.tail = Doubly()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.counter = 0
        self.capacity = capacity
        self.d = {}
        
    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]

        node.next.prev = node.prev
        node.prev.next = node.next
        
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        return node.v

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
    
            node.next.prev = node.prev
            node.prev.next = node.next
            
            self.tail.prev.next = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
            node.v = value

        else:
            if self.counter == self.capacity:
                temp = self.head.next
                self.head.next = temp.next
                self.head.next.prev = self.head
                del self.d[temp.k]
                self.counter -= 1
            node = Doubly(key, value)
            self.d[key] = node
            self.tail.prev.next = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
            self.counter += 1
    
    
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)