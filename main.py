# Author: Samuel Faubert
# ID: 001385881

import csv
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
    package_delivery_day.deliver_packages(package_delivery_day.truck3)
    
    package_delivery_day.total_miles = package_delivery_day.truck1.miles_traveled + package_delivery_day.truck2.miles_traveled + package_delivery_day.truck3.miles_traveled
    print('total miles: ' + str(package_delivery_day.total_miles)) 

    
    
    
    