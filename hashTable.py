import hashlib
from importlib.resources import Package
from tokenize import String


class HashTable:
    # Constructor for the hash table class which creates a new, blank hash table
    # Default capacity is 50
    # This is a chaining hash table, each bucket is initialized with an empty list - O(n)
    # space O(n) - the hash table contains as many lists as the initial capacity
    def __init__(self, initial_capacity=41):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def __len__(self) -> int:
        """length function for the hash table

        Returns:
            int: the size of the table
        """
        return len(self.table)
    # Insert function takes a node as the value to add to the hash table
    # The bucket to insert is retrieved from the modulo of the size of the hash table - O(n)
    # The node gets added to the list in the selected bucket - space O(n^2) the worst case scenario is that the hashing function puts all packages in the same bucket
    # in that case, the table would contain n empty buckets except one, which would contain all of the packages (n)
    def insert(self, id, package) -> bool:
        """Inserts a new package object into the hash table

        Args:
            id (String): the package id taken from the file
            package (Package): the package to add

        Returns:
            bool: returns True if the package was added successfully
        """
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

    # Lookup parameter returns the value in the bucket list for the given key parameter - O(n)
    def lookup(self, id) -> Package:
        """Lookup a package by ID in the packages hash table

        Args:
            id (string): the package ID to look for

        Returns:
            Package: the package with the specified ID
        """
        bucket = int(id) % len(self.table)
        bucket_list = self.table[bucket]
        for package_list in bucket_list:
            if package_list[0] == id:
                return package_list[1]
        else:
            return None


    # Remove function takes a key as the parameter and removes it from the bucket list if it is there - O(n)
    def delete(self, package) -> String:
        """Removes a package from the hash table

        Args:
            package (Package): the package to remove

        Returns:
            String: returns a string describing the result of the operation
        """
        bucket = int(package.id) % len(self.table)
        bucket_list = self.table[bucket]
        for package_list in bucket_list:
            if package_list[0] == package.id:
                bucket_list.remove(package_list)
                return "Package deleted"
        else:
            return "Package not found"

    # print objects in the hash table - O(n)
    def print_map(self):
        """Print all addresses listed in the table
        """
        for i in range(50):
            if len(self.table[i]) > 0:
                
                print(self.table[i][0][1].address)