from datetime import datetime, timedelta
from struct import pack

import package
import truck
import hashTable
import csv_helper
import pathlib

class Package_Delivery():
    csv_reader = None
    distance_data = None
    addresses_data = None
    packages_table = None
    # total miles traveled during the day
    

    # When a package is delivered, the delivery time will be saved as the key and the package ID as the value
    package_delivery_times = {}
    
    

    def __init__(self):
        self.csv_reader = csv_helper.CSV_helper()
        self.packages_table = hashTable.HashTable()
        data_path = pathlib.Path('/home/sam/DSA2/packageDeliveryWGUPS/data_files')
        
        # fill out the hash table with the package data
        self.csv_reader.load_package_data(data_path/"WGUPS Package File.csv", self.packages_table)
        # fill the distances list with all distances
        self.distance_data = self.csv_reader.load_distance_data(data_path/"distances.csv")
        # fill the address list with all addresses as strings
        self.addresses_data = self.csv_reader.load_addresses(data_path/"addresses.csv")

        self.total_miles = 0
        self.distance_to_next = 0
        # initialize truck1 with a driver
        self.truck1 = truck.Truck('Truck 1',True)
        # initiliaze truck2 with a driver
        self.truck2 = truck.Truck('Truck 2',True, start_hour=9, start_minute=5)
        # intialize truck3 without a driver
        self.truck3 = truck.Truck('Truck 3',False)
        self.current_time = datetime.today()
        self.day_start_time = self.current_time.time().replace(hour=8, minute=0,second=0,microsecond=0)
        self.day_end_time = self.current_time.time().replace(hour=16, minute=0,second=0,microsecond=0)
        

    def get_address_index(self, addr):
        for i in range(len(self.addresses_data)):
            if addr == self.addresses_data[i]:
                return i
        return 0

    def display_total_mileage(self):
        miles = round(self.truck1.miles_traveled + self.truck2.miles_traveled + self.truck3.miles_traveled, 2)
        print(f'Total distance traveled by all trucks: {miles} miles')

    def display_package_info(self, id):
        self.packages_table.lookup(id)

    def display_all_packages(self):
        size = (len(self.packages_table.table) - 1)
        for i in range(1, size):
            print(self.packages_table.table[i][0][1])

    # return the distance between 2 address
    def distance_between(self, addr1, addr2):
        addr1_index = None
        addr2_index = None
        count = 0
        # loop through all addresses in the list
        
        for addr in self.addresses_data:
            
            # When an address is found, assign the index of that address to the addr#_index variable
            if addr[1] == addr1:
                addr1_index = count
            if addr[1] == addr2:
                addr2_index = count
            # if both addresses have been found, break out of the loop
            if addr1_index is not None and addr2_index is not None:
                break
            count += 1

        # find the distance in the distances table by putting the larger index first to avoid getting empty data
        if addr2_index > addr1_index:
            return float(self.distance_data[addr2_index][addr1_index])
        else:
            return float(self.distance_data[addr1_index][addr2_index])
        

    def min_distance(self, truck):
        next_package = None
        self.distance_to_next = float(-1)

        # loop through all packages in the truck
        for package in truck.truck_packages:
            # if the next package to deliver has not been initialized, set it to the package in the list
            if next_package is None:
                next_package = package
            # if the distance is 0, set it to the distance from the current address to the address of the next_package
            if self.distance_to_next == -1:
               
                self.distance_to_next = self.distance_between(truck.current_location, package.address)
            # calculate the distance for each package in the truck and save the smallest one in the distance_to_next variable
            
            package_distance = self.distance_between(truck.current_location, package.address)
            
            if package_distance < self.distance_to_next:
                self.distance_to_next = package_distance
                next_package = package
        # return the package object that has the shortest distance to the next address
        
        return next_package
    
    # load all packages from the hash table into one of the 3 trucks
    def load_truck_packages(self):
        self.truck1.current_location = self.addresses_data[0][1]
        self.truck1.add_package(self.packages_table.table[1][0][1])

        # 4 and 40 share the same address
        self.truck1.add_package(self.packages_table.table[4][0][1])
        self.truck1.add_package(self.packages_table.table[40][0][1])
        # 39 and 13 share an address
        self.truck1.add_package(self.packages_table.table[13][0][1])
        self.truck1.add_package(self.packages_table.table[39][0][1])
        # package 14 must be delivered with 15 and 19
        self.truck1.add_package(self.packages_table.table[14][0][1])
        # 34, 15, and 16 share an address
        self.truck1.add_package(self.packages_table.table[15][0][1])
        # package 16 must be delivered with 13 and 19
        self.truck1.add_package(self.packages_table.table[16][0][1])
        self.truck1.add_package(self.packages_table.table[34][0][1])
        self.truck1.add_package(self.packages_table.table[19][0][1])
        # package 20 must be delivered with 13 and 15
        # 20 and 21 share the same address
        self.truck1.add_package(self.packages_table.table[20][0][1])
        self.truck1.add_package(self.packages_table.table[21][0][1])
        self.truck1.add_package(self.packages_table.table[24][0][1])
        self.truck1.add_package(self.packages_table.table[10][0][1])

        # 7 and 29 share the same address
        self.truck1.add_package(self.packages_table.table[7][0][1])
        self.truck1.add_package(self.packages_table.table[29][0][1])
        
                

        
        self.truck2.current_location = self.addresses_data[0][1]
        # package #3 can only be on truck 2
        self.truck2.add_package(self.packages_table.table[3][0][1])
        # package 6 delayed
        self.truck2.add_package(self.packages_table.table[6][0][1])
        
        # package #18 can only be on truck 2
        self.truck2.add_package(self.packages_table.table[18][0][1])
        # package 25 delayed
        # 25 and 26 share the same address
        self.truck2.add_package(self.packages_table.table[25][0][1])
        self.truck2.add_package(self.packages_table.table[26][0][1])

        # 8 and 30 share the same address
        self.truck2.add_package(self.packages_table.table[8][0][1])
        self.truck2.add_package(self.packages_table.table[30][0][1])   
        
        # 31 and 32 share the same address
        self.truck2.add_package(self.packages_table.table[31][0][1])
        # package 32 delayed
        self.truck2.add_package(self.packages_table.table[32][0][1])

        # package #36 can only be on truck 2
        self.truck2.add_package(self.packages_table.table[36][0][1])

        # 5, 37 and 38 share the same address
        # package #38 can only be on truck 2
        self.truck2.add_package(self.packages_table.table[37][0][1])
        self.truck2.add_package(self.packages_table.table[38][0][1])
        self.truck2.add_package(self.packages_table.table[5][0][1])
        
        self.truck2.add_package(self.packages_table.table[27][0][1])
        self.truck2.add_package(self.packages_table.table[35][0][1])


        self.truck3.current_location = self.addresses_data[0][1]

        # 2 and 33 share the same address
        self.truck3.add_package(self.packages_table.table[2][0][1])
        self.truck3.add_package(self.packages_table.table[33][0][1])

        
        
        self.truck3.add_package(self.packages_table.table[22][0][1])

        # 27 and 35 share the same address
        
        self.truck3.add_package(self.packages_table.table[11][0][1])
        self.truck3.add_package(self.packages_table.table[12][0][1])
        self.truck3.add_package(self.packages_table.table[17][0][1])
        self.truck3.add_package(self.packages_table.table[23][0][1])
        # wrong address listed package 9
        self.truck3.add_package(self.packages_table.table[9][0][1])
        # package 28 delayed
        self.truck3.add_package(self.packages_table.table[28][0][1])
        
        
        


    def deliver_packages(self, truck):
        # check if the truck has a driver assigned
        if truck.has_driver is False:
            print(truck.label + ' has no driver')
        # update all packages on the truck to 'en route' status
        else: 
            print(truck.label + ' going out for ' + str(truck.current_packages) + ' deliveries')
            for i in range(truck.current_packages):
                truck.truck_packages[i].delivery_status = 'en route'
            for i in range(truck.current_packages):
                # determine the next package to deliver using the greedy algorithm
                next_package = self.min_distance(truck)
                # move the truck to the next location
                truck.move_truck(float(self.distance_to_next), next_package.address)
                # deliver the package
                truck.deliver_package(next_package)
                # change the package status to delivered
                next_package.delivery_status = 'delivered'
                print(next_package)
                
                
        # calculate the distance to the hub and move the truck back to the hub
        if truck.current_packages == 0:
                 
            distance_to_hub = float(self.distance_between(truck.current_location, self.addresses_data[0][1]))
            truck.move_truck(distance_to_hub, self.addresses_data[0][1])
            truck.deliveries_complete_time = truck.day_start_time + timedelta(minutes=truck.time_elapsed)
            print(truck.label + ' is now back at the hub. The time is now: ' + str(truck.deliveries_complete_time))
            

