class doubly:
    
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    # we use hmap for constant indexing
    # we use doubly linkedlist for constant insertion and deletion
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {} 
        self.head = doubly(0, 0) 
        self.tail = doubly(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        
        if key in self.hmap:
            node = self.hmap[key]

            # delete node inplace
            node.prev.next = node.next
            node.next.prev = node.prev
            
            # insert node at head
            nextval = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = nextval
            nextval.prev = node

            return node.val

        return -1    

    def put(self, key: int, value: int) -> None:

        if key in self.hmap:
            node = self.hmap[key]

            # delete node inplace
            node.prev.next = node.next
            node.next.prev = node.prev

            # insert node at head
            nextval = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = nextval
            nextval.prev = node

            # update node.val
            node.val = value
        
        else:
            # deleting LRU key
            if len(self.hmap) >= self.capacity:

                node = self.tail.prev
                node.prev.next = self.tail
                self.tail.prev = node.prev
                del self.hmap[node.key]

            # inserting new key at head
            node = doubly(key, value)
            self.hmap[key] = node

            nextval = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = nextval
            nextval.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)