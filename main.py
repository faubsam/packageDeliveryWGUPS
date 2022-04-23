# Author: Samuel Faubert
# ID: 001385881

import csv
from struct import pack
import csv_helper
import hashTable
import package_delivery

 

if __name__ == "__main__":
    package_delivery_day = package_delivery.Package_Delivery()
    print("Starting deliveries for the day...........")
    package_delivery_day.load_truck_packages()
    
    print(package_delivery_day.truck1.current_packages)
    print(package_delivery_day.truck2.current_packages)
    print(package_delivery_day.truck3.current_packages)
    package_delivery_day.deliver_packages(package_delivery_day.truck1)
    package_delivery_day.deliver_packages(package_delivery_day.truck2)
    if package_delivery_day.truck1.current_packages == 0 and package_delivery_day.truck1.current_location == package_delivery_day.addresses_data[0][1]:
        print('Driver for truck 1 can now switch to a new truck')
    if package_delivery_day.truck2.current_packages == 0 and package_delivery_day.truck2.current_location == package_delivery_day.addresses_data[0][1]:
        print('Driver for truck 2 can now switch to a new truck')
    print('Driver assigned to truck 3')
    package_delivery_day.truck3.has_driver = True
    package_delivery_day.deliver_packages(package_delivery_day.truck3)
    
    package_delivery_day.total_miles = package_delivery_day.truck1.miles_traveled + package_delivery_day.truck2.miles_traveled + package_delivery_day.truck3.miles_traveled
    print('total miles: ' + str(int(package_delivery_day.total_miles))) 
    print(package_delivery_day.day_end_time)

    
    
    
    