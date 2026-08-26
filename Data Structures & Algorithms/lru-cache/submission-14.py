# make class for the node
class Node:
    def __init__(self, key, val):
        # each node is going to have a key value pair
        # so we initialize those
        self.key = key
        self.val = val

        # two pointers, one for next, one for prev
        self.prev = None
        self.next = None



class LRUCache:

    def __init__(self, capacity: int):
        # need to store capacity so we know if we go over
        self.cap = capacity

        # use hash map for cache
        self.cache = {} # map key to node

        # dummy nodes to tells what LRU and MRU is 
        # initialize them with 0s for the default values
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # initially we want these nodes to be connected
        # b/c if we insert a node, we want to put it in b/w them
        # Left = LRU, right = MRU
        self.left.next = self.right
        self.right.prev = self.left

    # helper functions for linked list

    # remove any node from list
    def remove(self, node):
        # so if you have 3 nodes and you want to remove the middle node
        # you take the node before the middle node next's pointer
        # and move it to the node after the middle node
        # then you take the node after the middle prev's pointer
        # and move it to the node before the middle node
        # this basically decouples the middle node from the list
        # there's nothing connecting to our list anymore
        # and we consider that as a removal

        # get prev and next nodes of middle node
        prev = node.prev
        nxt = node.next

        # decouple middle node from previous one
        prev.next = nxt

        # decouple middle node from next one
        nxt.prev = prev


    # insert any node at the rightmost position in our list
    # right before our right pointer dummy node
    def insert(self, node):
        # so we have the right node and the previous node before it
        # when we add our new node
        # we reassign our right node's previous pointer to the new node
        # and reassign the old previous node's next pointer to our new node
        # then we connect the new node to its neighbors
        # so we assign new node's next pointer to the right node
        # and assign new node's previous pointer to the old previous node
        # and this inserts the new node right in between them
        
        # get previous and next pointers from right dummy node
        prev = self.right.prev
        nxt = self.right

        # insert new node in b/w them
        prev.next = node
        nxt.prev = node

        # connect new node to its neighbors
        node.next = nxt
        node.prev = prev


    def get(self, key: int) -> int:
        # if the key is in our cache
        if key in self.cache:
            # take this node and remove it from our list
            self.remove(self.cache[key])

            # after we remove it then we want to reinsert it at the rightmost position
            self.insert(self.cache[key])

            # then we can return the our value,
            # which is the same as the key
            # but it still at the value of that key
            return self.cache[key].val

        # if it doesn't exist then return -1
        return -1
        

    def put(self, key: int, value: int) -> None:
        # if key already in our cache 
        if key in self.cache:
            # that means that a node already exists 
            # in our list with the same key value
            # so we want to remove this node from our list
            self.remove(self.cache[key])

        # now we can create a new node with this key value pair
        # and put that in our cache hashmap
        # mapping keys to nodes remember
        self.cache[key] = Node(key, value)

        # insert this node into our list 
        # to make it MRU
        self.insert(self.cache[key])

        # every we insert, we have to check capacity
        # AKA does the length of our cache now exceed capacity
        if len(self.cache) > self.cap:
            # if it does 
            # then we remove the LRU node from the list
            # and delete the LRU from our cache hashmap

            # now we find the node for the LRU
            # left pointer is all the way at the left
            # and it is going to tell us the LRU
            # and since left is a dummy node,
            # the lru is at it's next pointer
            lru = self.left.next

            # remove the LRU from our linked list
            self.remove(lru)

            # delete it from our cache hashmap
            # want the key of this node which is stored in the node itself
            del self.cache[lru.key]
        
