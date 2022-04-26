# Author: Samuel Faubert
# ID: 001385881

import csv
from datetime import datetime
from struct import pack
import csv_helper
import hashTable
import package_delivery

def print_menu():
    for i in range(3):
        print(" ")
    print('Please select one of 3 options')
    print('-----------------------------------')
    print('1 - Display total truck mileage')
    print('2 - Display current status of all packages')
    print('3 - Display current status for a select package')
    print('4 - Exit the application (all data will be lost)')
     

if __name__ == "__main__":
    package_delivery_day = package_delivery.Package_Delivery()
    print("Starting deliveries for the day...........")
    package_delivery_day.load_truck_packages()
    
    
    package_delivery_day.deliver_packages(package_delivery_day.truck1)
    package_delivery_day.deliver_packages(package_delivery_day.truck2)
    if package_delivery_day.truck1.current_packages == 0 and package_delivery_day.truck1.current_location == package_delivery_day.addresses_data[0][1]:
        print('Driver for truck 1 can now switch to a new truck')
    if package_delivery_day.truck2.current_packages == 0 and package_delivery_day.truck2.current_location == package_delivery_day.addresses_data[0][1]:
        print('Driver for truck 2 can now switch to a new truck')
    print('Driver assigned to truck 3')
    package_delivery_day.truck3.has_driver = True
    package_delivery_day.truck3.current_time = package_delivery_day.truck1.deliveries_complete_time
    package_delivery_day.truck3.day_start_time = package_delivery_day.truck1.deliveries_complete_time
    print("Truck 3 leaving at: " + str(package_delivery_day.truck3.current_time))
    package_delivery_day.deliver_packages(package_delivery_day.truck3)
    
    
    print_menu()
    user_choice = input('Enter your choice: ')
    
    while(user_choice is not '4'):
        if user_choice == '1':
            print('****************************************')
            package_delivery_day.display_total_mileage()
            print('****************************************')
        elif user_choice == '2':
            print('****************************************')
            package_delivery_day.display_all_packages()
            print('****************************************')
        elif user_choice == '3':
            print('****************************************')
            package_number = input(f'Enter the package ID to search for (ID cannot be greater than {len(package_delivery_day.packages_table.table) -1}): ')
            print('-----------------------------------------')
            package_delivery_day.display_package_info(package_number)
            print('****************************************')
        print_menu()    
        user_choice = input('Enter your choice: ') 
        if(user_choice == '4'):
            quit()