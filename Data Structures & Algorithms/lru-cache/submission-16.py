# create node class
class Node:
    # initialize with key and val 
    def __init__(self, key, val):
        # initialize key and val and pointers
        self.key = key
        self.val = val

        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        # initialize capacity, cache, and dummy pointers
        self.cap = capacity

        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # make dummy pointers point towards each other
        self.left.next = self.right
        self.right.prev = self.left

    # create remove and insert helper functions
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prev
        

    def get(self, key: int) -> int:
        # check if key exists 
        if key in self.cache:
            # if it does, then we return val
            # which is stored in that key's node
            
            # but since we used it, we want to make it MRU
            # so we remove the node at this key
            self.remove(self.cache[key])

            # and we insert it again so it becomes MRU
            self.insert(self.cache[key])

            # then we can return the val
            return self.cache[key].val

        # if key doesn't exist then return -1
        return -1


        

    def put(self, key: int, value: int) -> None:
        # check if key exists
        if key in self.cache:
            # if it does exist already
            # then we update the value
            # by removing it here and
            # we add it outside of this if
            # because we are going to add the new key regardless
            # and that would handle the adding of this removed key
            self.remove(self.cache[key])

        # add the new key after we removed the 
        # possible old one with an old value 
        self.cache[key] = Node(key, value)

        self.insert(self.cache[key])

        # check if we have exceeded capacity
        if len(self.cache) > self.cap:
            # then we remove lru
            # lru is the next pointer of the dummy left node
            lru = self.left.next

            # remove lru
            self.remove(lru)

            # lru is removed so now we delete it's key 
            # from our cache
            del self.cache[lru.key]
        
