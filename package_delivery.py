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
        addr1_index = None
        addr2_index = None

        # loop through all addresses in the list
        for addr in self.addresses_data:
            # When an address is found, assign the index of that address to the addr#_index variable
            if addr is addr1:
                addr1_index = self.addresses_data.index(addr)
            if addr is addr2:
                addr2_index = self.addresses_data.index(addr)
            # if both addresses have been found, break out of the loop
            if addr1_index is not None and addr2_index is not None:
                break
        # find the distance in the distances table by putting the larger index first to avoid getting empty data
        if addr2_index > addr1_index:
            return self.distance_data[addr2_index][addr1_index]
        else:
            return self.distance_data[addr1_index][addr2_index]
        

    def min_distance(self, addr, truck):
        next_package = None
        distance_to_next = 0

        # loop through all packages in the truck
        for package in truck.truck_packages:
            # if the next package to deliver has not been initialized, set it to the package in the list
            if next_package is None:
                next_package = package
            # if the distance is 0, set it to the distance from the current address to the address of the next_package
            if distance_to_next == 0:
                distance_to_next = self.distance_between(truck.current_location, package.address)
            # calculate the distance for each package in the truck and save the smallest one in the distance_to_next variable
            package_distance = self.distance_between(truck.current_location, package.address)
            if package_distance < distance_to_next:
                distance_to_next = package_distance
                next_package = package
        # return the package object that has the shortest distance to the next address
        return next_package
    
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
        
            

