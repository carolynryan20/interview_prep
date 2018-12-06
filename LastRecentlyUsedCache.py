class Node():
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.hashtable = {}
        self.head_linkedlist = Node("dummy", 0)
        self.tail_linkedlist = Node("dummy", 0)
        self.head_linkedlist.next = self.tail_linkedlist
        self.tail_linkedlist.prev = self.head_linkedlist

    def put(self, key, value):
        if key in self.hashtable:
            # Update linked list with this key at the beginning
            # Update the value so thats its the correct
            original_node = self.hashtable[key]
            original_node.val = value
            original_node.prev.next = original_node.next
            original_node.next.prev = original_node.prev

            original_node.next = self.head_linkedlist.next
            original_node.prev = self.head_linkedlist
            self.head_linkedlist.next = original_node
            return True

        else:
            # Add a new node to the cache
            # Update size, check if we need need to remove from cache
            new_node = Node(key, value)
            if self.size >= self.capacity:
                if self.tail_linkedlist.prev == self.head_linkedlist:
                    print("Wanting to delete dummy, can't")
                    return False
                else:
                    to_delete = self.tail_linkedlist.prev
                    to_delete.prev.next = self.tail_linkedlist
                    self.tail_linkedlist.prev = to_delete.prev
                    del self.hashtable[to_delete.key]
                    self.size -= 1

            new_node.next = self.head_linkedlist.next
            new_node.prev = self.head_linkedlist
            new_node.next.prev = new_node
            self.head_linkedlist.next = new_node

            self.hashtable[key] = new_node
            self.size += 1

    def get(self, key):
        if key in self.hashtable:
            # Return value
            # Update linked list with this key at the beginning
            # Update the value so thats its the correct
            original_node = self.hashtable[key]
            original_node.prev.next = original_node.next
            original_node.next.prev = original_node.prev

            original_node.next = self.head_linkedlist.next
            original_node.prev = self.head_linkedlist
            self.head_linkedlist.next = original_node
            return original_node.val
        return None

    def _move_node_to_front(self, node, value = None):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.head_linkedlist.next
        node.prev = self.head_linkedlist
        self.head_linkedlist.next = node

    def __str__(self):
        s = ''
        cur = self.head_linkedlist.next
        while cur and cur.key != 'dummy':
            s += '({}: \'{}\') -> '.format(cur.key, cur.val)
            cur = cur.next
        if s != '':
            return s[:-4]
        return s

def main():
    cache = LRUCache(3)

    cache.put(1, 'a')  # [(1, ‘a’)]
    print(cache)
    cache.put(2, 'b')  # [(2, ‘b’), (1, ‘a’)]
    print(cache)

    cache.put(3, 'c')  # [(3, ‘c’), (2, ‘b’), (1, ‘a’)]
    print(cache)

    cache.put(4, 'd')  # [(4, ‘d’), (3, ‘c’), (2, ‘b’)]
    print(cache)

    print(cache.get(1))  # return None
    print(cache)

    print(cache.get(3))  # return ‘c’; [(3, ‘c’), (4, ‘d’), (2, ‘b’)]
    print(cache)

    cache.put(2, 'e')  # [(2, ‘e’), (3, ‘c’), (4, ‘d’)]
    print(cache)

main()


'''
Please use this Google doc to code during your interview. To free your hands for coding, we recommend that you use a headset or a phone with speaker option.

Least recently used cache

class LRUCache:
 def __init__(self, capacity):
 def put(self, k, v):
 def get(self, k):

cache = LRUCache(3)
cache.put(1, ‘a’)  # [(1, ‘a’)]
cache.put(2, ‘b’)  # [(2, ‘b’), (1, ‘a’)]
cache.put(3, ‘c’)  # [(3, ‘c’), (2, ‘b’), (1, ‘a’)]
cache.put(4, ‘d’)  # [(4, ‘d’), (3, ‘c’), (2, ‘b’)]
cache.get(1)       # return None
cache.get(3)       # return ‘c’; [(3, ‘c’), (4, ‘d’), (2, ‘b’)]
cache.put(2, ‘e’)  # [(2, ‘e’), (3, ‘c’), (4, ‘d’)]

1.	queue (fifo): issue when updating key/value
2.	hash table: not order
3.	linked list:
a.	singly linked list with a pointer to the tail
i.	put ~ O(N)
ii.	get ~ O(N)
b.	doubly linked list

a -> b -> c -> d -> e
1.	head = c
2.	c -> a -> b -> d -> e

class Node():
	def __init__(self, key, val, prev = None, next = None):
		self.key = key
		self.val = val
		self.prev = prev
		self.next = next

class LRUCache():
	def __init__(self, capacity):
		self.capacity = capacity
		self.size = 0
		self.hashtable = {}
		self.head_linkedlist = None
		self.tail_linkedlist = None

	def put(self, key, value):
		if key in self.hashtable:
			# Update linked list with this key at the beginning
			# Update the value so thats its the correct
			original_node = self.hashtable[key]
			original_node.val = value
			original_node.prev.next = original_node.next
			original_node.next.prev = original_node.prev
			original_node.next = self.head_linkedlist
			original_node.prev = None
			self.head_linkedlist = original_node
			return True
		else:
			# Add a new node to the cache
			# Update size, check if we need need to remove from cache
			new_node = Node(key, value)
			if self.size >= self.capacity:
				self.tail_linkedlist.prev = None
				del self.hashtable[self.tail_linkedlist.key]
				self.size -= 1
			self.head_linkedlist.prev = new_node
			new_node.next = self.head_linkedlist
			self.head_linkedlist = new_node
			self.hashtable[key] = new_node
			self.size += 1
				
dummy_head <-> … <-> dummy_tail



'''