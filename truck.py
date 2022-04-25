from datetime import datetime, timedelta

import package_delivery




class Truck:
    max_packages = 16
    speed = 18
    # list of all packages that been loaded onto the truck
    truck_packages = []
    # address where the truck is currently located
    current_location = None
    # number of package that are currently loaded on the truck
    current_packages = 0
    # there are more trucks than drivers, so this tells us whether or not the truck currently has a driver assigned
    has_driver = False
    # the miles traveled by the truck during the day
    miles_traveled = 0
    # the time it takes to deliver the next package on the truck
    time_to_deliver = 0
    # the total time in minutes since the truck has left the hub facility
    time_elapsed = 0
    label = ""
    day_start_time = datetime.now().replace(hour=8, minute=0,second=0,microsecond=0)
    current_time = day_start_time
    deliveries_complete_time = day_start_time + timedelta(minutes=time_elapsed)

    def __init__(self, label, has_driver, max_packages=max_packages, speed=speed):
        self.max_packages = max_packages
        self.speed = speed
        self.has_driver = has_driver
        self.label = label
        

    # load a package onto the truck and update the current packages count
    def add_package(self, package):
        if self.current_packages >= self.max_packages:
            print("Package limit reached for this truck. Cannot add package with id: " + package.id) 
        else:
            self.truck_packages.append(package)
            self.current_packages += 1

    # move to the truck to a new address and update the truck's location
    def move_truck(self, distance, dest_addr):
        if self.has_driver is False:
            print("Truck has no driver")
        else:
            # calculate the distance to the next delivery address
            distance_to_next_stop = distance
            # update the miles traveled by this truck
            self.miles_traveled += distance_to_next_stop
            # calculate the time to deliver the next package
            self.time_to_deliver = (distance/self.speed)*60
            # update the total time elapsed since the truck left the hub
            self.time_elapsed += self.time_to_deliver
            # update the truck's location to the next delivery address
            self.current_location = dest_addr

    def deliver_package(self, package):
        if self.has_driver is False:
            print("Truck has no driver")
        else: 
            count = 0
            # remove the package from the truck's list of packages
            for pack in self.truck_packages:
                if pack.id == package.id:
                    self.truck_packages.remove(pack)
                count += 1
                # timestamp the package delivery
                pack.delivery_time = self.current_time + timedelta(minutes=self.time_to_deliver)
            # update the count of packages currently in the truck
            self.current_packages -= 1
            # update the current_time tracker
            self.current_time += timedelta(minutes=self.time_to_deliver)
            

    