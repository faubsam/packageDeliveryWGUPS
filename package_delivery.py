from struct import pack
import package
import truck
import hashTable
import csv_helper

class Package_Delivery():
    csv_reader = None
    distance_data = None
    addresses_data = None
    packages_table = None
    # total miles traveled during the day
    total_miles = 0
    
    # initialize truck1 with a driver
    truck1 = truck.Truck(True)
    # initiliaze truck2 with a driver
    truck2 = truck.Truck(True)
    # intialize truck3 without a driver
    truck3 = truck.Truck(False)
    
    

    def __init__(self):
        self.csv_reader = csv_helper.CSV_helper()
        self.packages_table = hashTable.HashTable()
        # fill out the hash table with the package data
        self.csv_reader.load_package_data("DSA2/packageDeliveryWGUPS//data_files/WGUPS Package File.csv", self.packages_table)
        # fill the distances list with all distances
        self.distance_data = self.csv_reader.load_distance_data("/home/sam/DSA2/packageDeliveryWGUPS/data_files/distances.csv")
        # fill the address list with all addresses as strings
        self.addresses_data = self.csv_reader.load_addresses("/home/sam/DSA2/packageDeliveryWGUPS/data_files/addresses.csv")
    
          
    # return the distance between 2 address
    def distance_between(self, addr1, addr2):
        return self.distance_data[self.addresses_data.index(addr1)][self.addresses_data.index(addr2)]

    def min_distance(self, addr, truck):
        next_package = None
        distance_to_next = 0

        for package in truck.truck_packages:
            if next_package is None:
                next_package = package
            if distance_to_next == 0:
                distance_to_next = package
            
    
    # load all packages from the hash table into one of the 3 trucks
    def load_truck_packages(self):
        self.truck1.add_package(self.packages_table.table[1][0][1])
        self.truck1.add_package(self.packages_table.table[4][0][1])
        self.truck1.add_package(self.packages_table.table[7][0][1])    
        self.truck1.add_package(self.packages_table.table[13][0][1])
        self.truck1.add_package(self.packages_table.table[14][0][1])
        self.truck1.add_package(self.packages_table.table[15][0][1])
        self.truck1.add_package(self.packages_table.table[16][0][1])
        self.truck1.add_package(self.packages_table.table[19][0][1])
        self.truck1.add_package(self.packages_table.table[20][0][1])
        self.truck1.add_package(self.packages_table.table[21][0][1])
        self.truck1.add_package(self.packages_table.table[22][0][1])
        self.truck1.add_package(self.packages_table.table[24][0][1])
        self.truck1.add_package(self.packages_table.table[29][0][1])
        self.truck1.add_package(self.packages_table.table[34][0][1])
        self.truck1.add_package(self.packages_table.table[39][0][1])
        self.truck1.add_package(self.packages_table.table[40][0][1])

        
        self.truck2.add_package(self.packages_table.table[3][0][1])
        self.truck2.add_package(self.packages_table.table[5][0][1])
        self.truck2.add_package(self.packages_table.table[6][0][1])
        self.truck2.add_package(self.packages_table.table[8][0][1])
        self.truck2.add_package(self.packages_table.table[12][0][1])
        self.truck2.add_package(self.packages_table.table[18][0][1])
        self.truck2.add_package(self.packages_table.table[25][0][1])
        self.truck2.add_package(self.packages_table.table[26][0][1])
        self.truck2.add_package(self.packages_table.table[27][0][1])
        self.truck3.add_package(self.packages_table.table[30][0][1])
        self.truck2.add_package(self.packages_table.table[31][0][1])
        self.truck2.add_package(self.packages_table.table[32][0][1])
        self.truck2.add_package(self.packages_table.table[35][0][1])
        self.truck2.add_package(self.packages_table.table[36][0][1])
        self.truck2.add_package(self.packages_table.table[37][0][1])
        self.truck2.add_package(self.packages_table.table[38][0][1])

        self.truck3.add_package(self.packages_table.table[2][0][1])
        self.truck3.add_package(self.packages_table.table[9][0][1])
        self.truck3.add_package(self.packages_table.table[10][0][1])
        self.truck3.add_package(self.packages_table.table[11][0][1])
        self.truck3.add_package(self.packages_table.table[17][0][1])
        self.truck3.add_package(self.packages_table.table[23][0][1])
        self.truck3.add_package(self.packages_table.table[28][0][1])
        self.truck3.add_package(self.packages_table.table[33][0][1])


    def deliver_packages(self, truck):
        closest_address = None

