# Author: Samuel Faubert
# ID: 001385881

import csv
from itertools import islice
import csv_helper

    



class Truck:
    max_packages = 16
    speed = 18
    truck_packages = []

    def __init__(self, max_packages=max_packages, speed=speed):
        self.max_packages = max_packages
        self.speed = speed

    
    def add_package(self, package):
        self.truck_packages.append(package)


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
    def insert(self, id, package):
        bucket = hash(id) % len(self.table)
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
    def lookup(self, package):
        bucket = hash(package) % len(self.table)
        bucket_list = self.table[bucket]
        if package in bucket_list:
            node_index = bucket_list.index(package)
            return bucket_list[node_index]
        else:
            return None


    # Remove function takes a key as the parameter and removes it from the bucket list if it is there
    def delete(self, package):
        bucket = hash(package) % len(self.table)
        bucket_list = self.table[bucket]
        if package in bucket_list:
            bucket_list.remove(package)

    def print_map(self):
        for i in range(50):
            if len(self.table[i]) > 0:
                
                print(self.table[i][0][1].address)
    


if __name__ == "__main__":
    csv_reader = csv_helper.CSV_helper()


    packagesTable = HashTable()
    csv_reader.load_package_data("DSA2/packageDeliveryWGUPS//data_files/WGUPS Package File.csv", packagesTable)
    distance_data = csv_reader.load_distance_data("/home/sam/DSA2/packageDeliveryWGUPS/data_files/distances.csv")
    addresses_data = csv_reader.load_addresses("/home/sam/DSA2/packageDeliveryWGUPS/data_files/addresses.csv")
    
    