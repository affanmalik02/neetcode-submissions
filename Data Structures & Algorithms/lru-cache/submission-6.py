class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key to node 
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail # LRU
        self.tail.prev = self.head # MRU

    # insert at tail
    def insert(self, node):
        prev = self.tail.prev
        nxt = self.tail
        prev.next = node
        node.next = nxt
        node.prev = prev
        nxt.prev = node

    # remove node
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            ret = self.cache[key].value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return ret

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
            if len(self.cache) > self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.cache[lru.key]



