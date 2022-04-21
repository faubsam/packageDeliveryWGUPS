class Truck:
    max_packages = 16
    speed = 18
    truck_packages = []
    current_location = None
    current_packages = 0
    driver = None

    def __init__(self,  driver, max_packages=max_packages, speed=speed):
        self.max_packages = max_packages
        self.speed = speed
        self.driver = driver
        

    
    def add_package(self, package):
        if self.current_packages >= self.max_packages:
            print("Package limit reached for this truck. Cannot add package with id: " + package.id) 
        else:
            self.truck_packages.append(package)
            self.current_packages += 1

    def move_truck(self, dest_addr):
        self.current_location = dest_addr