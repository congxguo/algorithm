# state:
# - map: for fast search
# - linkedlist: for sorting by last access time
# - capacity: when to replace

# api:
# put - add a kv item to cache or update an existing one
# get - get a kv item from cache
# delete - remove a kv item from che


class Node():
    def __init__(self, k=None, v=None):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None
        
        


class LRU():
    def __init__(self, capacity):
        # control when to replace (memory management)
        self.capacity = capacity
        self.used = 0
        
        # index for quick search
        self.cache = dict()
        
        # double linked list
        self.head = Node("head", -1)
        self.tail = Node("tail", -1)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None
    
    def put(self, k, v):
        if k in self.cache:
            old_node = self.cache[k]
            self.remove_from_list(old_node)
            del self.cache[k]
            self.used -= 1
                
        if len(self.cache) == self.capacity:
            oldest_node = self.tail.prev
            print(f'oldest_node={oldest_node.k} -> {oldest_node.v}')
            self.remove_from_list(oldest_node)
            del self.cache[oldest_node.k]
            self.used -= 1
            
        node = Node(k, v)
        self.add_to_list(node)
        self.cache[k] = node
        self.used += 1
        print(f'capacity={self.capacity}, used={self.used}')
        self.debug()
    
    def get(self, k):
        if k not in self.cache:
            return None

        node = self.cache[k]
        self.remove_from_list(node)
        self.add_to_list(node)
        
        return node
    
    def remove(self, k):
        if k not in self.cache:
            return
        
        node = self.cache[k]
        self.remove_from_list(node)
        del self.cache[k]
        self.capacity -= 1
        
        
    # separate the ops on the list
    def remove_oldest_from_list(self):
        oldest_node = self.tail.prev
        self.remove_from_list(oldest_node)
    
    
    def remove_from_list(self, node):
        node.prev.next = node.next
        node.next.prev= node.prev
        
    
    def add_to_list(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        
        node.prev = self.head
        self.head.next = node
    
    
    def debug(self):
        node = self.head
        while node.next is not None:
            node = node.next
            print(f'{node.k} -> {node.v}')
        
    
lru_cache = LRU(3)
lru_cache.put('a', 1)
lru_cache.put('b', 2)
lru_cache.put('c', 3)
lru_cache.put('d', 4)
print(f'{lru_cache.get('a')}')
    