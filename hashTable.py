import hashlib


class HashTable:
    # Constructor for the hash table class which creates a new, blank hash table
    # Default capacity is 50
    # This is a chaining hash table, each bucket is initialized with an empty list
    def __init__(self, initial_capacity=41):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def __len__(self):
        return len(self.table)
    # Insert function takes a node as the value to add to the hash table
    # The bucket to insert is retrieved from the modulo of the size of the hash table
    # The node gets added to the list in the selected bucket
    def insert(self, id, package):
        bucket = int(id) % len(self.table)
        new_package = [id, package]

        if self.table[bucket] is None:
            self.table[bucket] = list([new_package])
            return True
        else:
            for bucket_list in self.table[bucket]:
                if bucket_list == id:
                    bucket_list[1] = package
                    return True
            self.table[bucket].append(new_package)
            return True

    # Lookup parameter returns the value in the bucket list for the given key parameter
    def lookup(self, id):
        bucket = int(id) % len(self.table)
        bucket_list = self.table[bucket]
        for package_list in bucket_list:
            if package_list[0] == id:
                return package_list[1]
        else:
            return None


    # Remove function takes a key as the parameter and removes it from the bucket list if it is there
    def delete(self, package):
        bucket = int(package.id) % len(self.table)
        bucket_list = self.table[bucket]
        for package_list in bucket_list:
            if package_list[0] == package.id:
                bucket_list.remove(package_list)
                return "Package deleted"
        else:
            return "Package not found"

    def print_map(self):
        for i in range(50):
            if len(self.table[i]) > 0:
                
                print(self.table[i][0][1].address)