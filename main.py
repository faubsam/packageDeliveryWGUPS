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
    
    
    