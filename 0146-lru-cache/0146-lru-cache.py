class doubly:
    
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.dic = dict()
        self.head = doubly(0, 0)
        self.tail = doubly(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        
        if key in self.dic:
            node = self.dic[key]
            
            node.prev.next = node.next
            node.next.prev = node.prev
            
            nextval = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = nextval
            nextval.prev = node
            
            return node.val
        
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.dic:
            node = self.dic[key]
            
            node.prev.next = node.next
            node.next.prev = node.prev
            
            nextval = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = nextval
            nextval.prev = node
            
            node.val = value
        
        else:
            if len(self.dic) >= self.capacity:
                
                temp = self.tail.prev
                self.tail.prev = temp.prev
                temp.prev.next = self.tail
                del self.dic[temp.key]
                
            node = doubly(key, value)
            self.dic[key] = node

            nextval = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = nextval
            nextval.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)