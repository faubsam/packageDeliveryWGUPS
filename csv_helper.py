import csv
from package import Package

class CSV_helper:

    def __init__(self) -> None:
        pass
    def load_distance_data(self, file):
        with open(file) as distances_file:
            distance_data = list(csv.reader(distances_file, delimiter=","))
        return distance_data

    def load_addresses(self, file):
        addresses_data = []
        with open(file, newline='') as addresses_file:
            for row in csv.reader(addresses_file):
                addresses_data.append(row)
                
        return addresses_data

    def load_package_data(self, file, hashTable):
        with open(file) as package_file:
            packageData = csv.reader(package_file, delimiter=",")
           
            for package in packageData:
                p_id = package[0]
                p_address = package[1]
                p_deadline = package[5]
                p_city = package[2]
                p_zip_code = package[4]
                p_weight = package[6]
                p_delivery_status = "At hub facility"

                p_package = Package(p_id, p_address, p_deadline, p_city, p_zip_code, p_weight, p_delivery_status)
                
                hashTable.insert(p_id, p_package)