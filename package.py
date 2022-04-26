


import csv
from dataclasses import replace
from datetime import datetime
from tokenize import String


class Package:
    id = 0
    address = ""
    deadline = "" 
    city = ""
    zip_code = ""
    weight = 0
    delivery_status = ""
    delivery_time = None

    # Constructor for package object with all required parameters from the requirements
    def __init__(self, id, address, deadline, city, zip_code, weight, delivery_status="At hub facility"):
        self.id = id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.delivery_status = delivery_status
        self.delivery_time = None

    # string method to print the packages in a readable format with relevant information
    def __str__(self) -> String:
        """str method to display package object in a readable format with relevant information

        Returns:
            String: returns the string to print
        """
        if self.delivery_status != 'delivered':
            return f'Package ID: {self.id}      deadline: {self.deadline}           status: {self.delivery_status}                                              delivery address: {self.address}'
        else:
            return f'Package ID: {self.id}      deadline: {self.deadline}           status: {self.delivery_status} at {self.delivery_time.time()}               delivery address: {self.address}'

    # add all packages in the file to the hash table - O(n)
    def loadPackageData(file, hashTable):
        """loads data from the packages file into the hash table

        Args:
            file (CSV file): csv file containing the package data
            hashTable (bool): the hash table to hold the package data
        """
        with open(file) as package_file:
            packageData = csv.reader(package_file)
            next(packageData)
            for package in packageData:
                p_id = package[0]
                p_address = package[1]
                p_deadline = package[5]
                p_city = package[2]
                p_zip_code = package[4]
                p_weight = package[6]

                p_package = Package(p_id, p_address, p_deadline, p_city, p_zip_code, p_weight)

                hashTable.insert(p_id, p_package)


