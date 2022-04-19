from os import remove


class HashTable:
    # Constructor for the hash table class which creates a new, blank hash table
    # Default capacity is 50
    # This is a chaining hash table, each bucket is initialized with an empty list
    def __init__(self, initial_capacity=50):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Insert function takes a node as the value to add to the hash table
    # The bucket to insert is retrieved from the modulo of the size of the hash table
    # The node gets added to the list in the selected bucket
    def insert(self, node):
        bucket = hash(node) % len(self.table)
        bucket_list = self.table[bucket]
        bucket_list.append(node)

    # Lookup parameter returns the value in the bucket list for the given key parameter
    def lookup(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        if key in bucket_list:
            node_index = bucket_list.index(key)
            return bucket_list[node_index]
        else:
            return None


    # Remove function takes a key as the parameter and removes it from the bucket list if it is there
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        if key in bucket_list:
            bucket_list.remove(key)
