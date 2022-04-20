class Truck:
    max_packages = 16
    speed = 18
    truck_packages = []

    def __init__(self, max_packages=max_packages, speed=speed):
        self.max_packages = max_packages
        self.speed = speed

    
    def add_package(self, package):
        self.truck_packages.append(package)