class Node:
    
    # Each node will have a key value pair as the data
    def __init__(self, key, val):
        self.key = key
        self.val = val
        # Pointer for previous node
        self.prev = None
        # Pointer for next node
        self.next = None
    
    
class LRUCache:
    # Helper method to insert a new node

    def __init__(self, capacity: int):
        
        # Maximum capacity of the cache
        self.capacity = capacity;
        
        # Dictionary to keep track of keys and pointer to their respective nodes in the linked list
        # We won't keep a value for a key in the dictionary
        # We will keep a pointer to the node
        # Because if we already have a pointer, we can get the previous and next node in O(1) time
        self.cache = {}
        
        # Doubly Linked list to keep track of previous and next nodes of any node
        # Initilly, we will have two dummy nodes, head and tail
        # Just like how we have a single dummy node when we create a new normal linked list
        
        self.head = Node(0,0)
        self.tail = Node(0,0)
        
        # Initially, the node next to head node is the tail
        self.head.next = self.tail
        
        # The node previous to the tail node is the head
        self.tail.prev = self.head
    
    # Helper method to break a node from its current place
    def breakNode(self, node):
        prev = node.prev
        next = node.next
        
        prev.next = next
        next.prev = prev
        
        
    # Helper method to put node just before the tail node
    def putBeforeTail(self, node):
        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node
    
    def get(self, key: int) -> int:
        
        # If the key does not exist, return -1
        if key not in self.cache: return -1
        
        # Since this is now the most recently used key
        # It should now be moved to the end of the linked list
        # And should be placed just before the tail
        
        # Break this node from its current point
        self.breakNode(self.cache[key])
        
        # Place it before the tail
        self.putBeforeTail(self.cache[key])
        
        # Return the value at this node in the linked list
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        
        # If the key exists
        if key in self.cache:
            
            # Update the value at this node
            self.cache[key].val = value
            
            # And since this is now the most recently used node
            # It will be moved to the end of the linked list, just before the tail
            
            # Break this node from its current point
            self.breakNode(self.cache[key])

            # Place it before the tail
            self.putBeforeTail(self.cache[key])

        # If the key does not exist already
        else:
            # If capacity is already full
            if len(self.cache) == self.capacity:
                # We have to remove the least recently used key
                
                # Remove it from the dictionary/cache
                self.cache.pop(self.head.next.key)
                
                # The least recently used key is always the next to the head node
                # So, break it from its place so as to remove it
                self.breakNode(self.head.next)
            
            # Now we can push a new node to the end with the given value
            newNode = Node(key,value)
            self.putBeforeTail(newNode)
                
            # Update the dictionary as well
            self.cache[key] = newNode