import package
import truck
import hashTable
import csv_helper

class Package_Delivery():
    csv_reader = None
    distance_data = None
    addresses_data = None
    packages_table = None
    total_miles = 0
    driver1 = "First Driver"
    driver2 = "Second Driver"
    truck1 = truck.Truck(driver1)
    truck2 = truck.Truck(driver2)
    truck3 = truck.Truck(driver1)
    

    def __init__(self):
        self.csv_reader = csv_helper.CSV_helper()
        self.packages_table = hashTable.HashTable()
        self.csv_reader.load_package_data("DSA2/packageDeliveryWGUPS//data_files/WGUPS Package File.csv", self.packages_table)
        
        self.distance_data = self.csv_reader.load_distance_data("/home/sam/DSA2/packageDeliveryWGUPS/data_files/distances.csv")
        self.addresses_data = self.csv_reader.load_addresses("/home/sam/DSA2/packageDeliveryWGUPS/data_files/addresses.csv")
    
          

    def distance_between(self, addr1, addr2):
        return self.distance_data[self.addresses_data.index(addr1)][self.addresses_data.index(addr2)]

    def min_distance(self, addr, packages):
        pass

    def load_truck_packages(self):
        self.truck2.add_package(self.packages_table.table[3][0][1])
        self.truck2.add_package(self.packages_table.table[26][0][1])
        self.truck2.add_package(self.packages_table.table[36][0][1])
        self.truck2.add_package(self.packages_table.table[38][0][1])
        

    def deliver_packages(self, truck):
        pass
